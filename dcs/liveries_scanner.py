import os
import re
import zipfile

from dcs.installation import get_dcs_install_directory, get_dcs_saved_games_directory
from typing import Optional, Dict, Iterator


class Liveries:
	"""
	Class containing a map of all units with their respective liveries.
	Each livery has a set of countries to indicate applicability
	"""

	map: Dict[str, Dict[str, set[str] | None]] = {}
	"""
	A dictionary containing all liveries for each unit.
	Mind that the unit uses the name of the livery folder, and not the ID.
	Every livery has a set of countries for which the livery is applicable.
	In case countries is None, it indicates the livery is valid for all countries

	Unit (str) -> {Livery (str) -> CountrySet (set[str]) | None}
	"""

	def __init__(self) -> None:
		"""
		Constructor for Liveries shouldn't be used explicitly.
		Initialization happens upon import.
		"""
		if len(Liveries.map) == 0:
			Liveries.scan_dcs_installation()
			Liveries.scan_custom_liveries()

	def __getitem__(self, unit: str) -> Optional[Dict[str, set[str] | None]]:
		return Liveries.map.get(unit)

	def __setitem__(self, unit: str, liveries: Dict[str, set[str] | None]) -> None:
		if unit in Liveries.map:
			Liveries.map[unit].update(liveries)
		else:
			Liveries.map[unit] = liveries

	def __delitem__(self, unit: str) -> None:
		del Liveries.map[unit]

	def __iter__(self) -> Iterator[str]:
		return Liveries.map.__iter__()

	@staticmethod
	def add_or_append(unit: str, livery_name: str, country: Optional[str] = None) -> None:
		"""
		Appends country to the specified livery for the specified unit,
		or creates a new set with the given country if the livery wasn't seen before
		If country is None, it indicates the livery is valid for all countries.

		:param unit: The name of the unit as 'DCS type',
			i.e. name of the unit inside the Liveries folder, e.g. 'A-10CII'
		:param livery_name: The name of the livery, e.g. '25th FS Osan AB, Korea (OS)'
		:param country: Shorthand name of a country indicating applicability for the given livery.
			'None' indicates all countries are valid for the given livery.
		"""
		if livery_name in Liveries.map[unit]:
			if country is not None:
				Liveries.map[unit][livery_name].add(country)
		else:
			Liveries.map[unit][livery_name] = country if country is None else {country}

	@staticmethod
	def scan_lua_code(luacode: str, path: str, unit: str) -> None:
		"""
		Scans the given code (expecting contents from a description.lua file)
		to extract the name of the livery together with the countries for which the livery is applicable.
		If no name is found, it defaults to the folder-name like DCS would.
		If no countries are found, it means the livery is valid for all countries.

		:param luacode: The contents of description.lua for the livery in question
		:param path: The path of the livery in question
		:param unit: The name of the unit as 'DCS type',
			i.e. name of the unit inside the Liveries folder, e.g. 'A-10CII'
		"""
		match = re.search(r'name\s*=\s*"(.*)"', luacode)
		if match is not None:
			livery_name = match.group(1)
		else:
			livery_name = path.split('\\')[-1].replace(".zip", "")

		match = re.search(r"countries\s*=\s*(\{.*\})", luacode)
		if match is not None:
			sanitizer = {"{": "", "}": "", "\"": "", " ": ""}
			translation = str.maketrans(sanitizer)
			country_list = match.group(1).translate(translation).split(',')
			countries = set(filter(lambda x: x != "", country_list))
			for country in countries:
				Liveries.add_or_append(unit, livery_name, country)
		else:
			Liveries.add_or_append(unit, livery_name)

	@staticmethod
	def scan_lua_description(path: str, unit: str) -> None:
		"""
		Verifies a description file exists and reads its contents,
		passing it to 'scan_lua_code'.

		:param path: The path of the livery in question
		:param unit: The name of the unit as 'DCS type',
			i.e. name of the unit inside the Liveries folder, e.g. 'A-10CII'
		"""
		description_path = os.path.join(path, "description.lua")
		if os.path.exists(description_path):
			with open(description_path, "r", encoding="utf-8") as file:
				code = file.read()
				Liveries.scan_lua_code(code, path, unit)

	@staticmethod
	def scan_zip_file(path: str, unit: str) -> None:
		"""
		Some liveries are zipped, this does the same as 'scan_lua_description',
		except for the fact it needs to "open the zip" first.

		:param path: The path of the livery in question
		:param unit: The name of the unit as 'DCS type',
			i.e. name of the unit inside the Liveries folder, e.g. 'A-10CII'
		"""
		if os.path.exists(path):
			with zipfile.ZipFile(path, 'r') as zf:
				if "description.lua" in zf.namelist():
					with zf.open("description.lua", "r") as file:
						code = file.read().decode("utf-8")
						Liveries.scan_lua_code(code, path, unit)

	@staticmethod
	def scan_liveries(path: str) -> None:
		"""
		Scans liveries for all units in the given path.

		:param path: A 'Liveries' path containing one or more units
		"""
		for unit in os.listdir(path):
			# The unit's name for liveries is NOT case-sensitive
			# thus convert 'unit' to upper/lower to make sure everything "merges properly"
			unit = unit.upper()
			if "COCKPIT" in unit:
				# Some custom mods put their cockpit liveries in the same directory,
				# for the time being we don't want to load those...
				continue
			if unit not in Liveries.map:
				Liveries.map[unit.upper()] = {}
			liveries_path = os.path.join(path, unit)
			for livery in os.listdir(liveries_path):
				livery_path = os.path.join(liveries_path, livery)
				if os.path.isdir(livery_path):
					Liveries.scan_lua_description(livery_path, unit)
				elif os.path.isfile(livery_path) and ".zip" in livery_path:
					Liveries.scan_zip_file(livery_path, unit)

	@staticmethod
	def scan_mods_path(path: str) -> None:
		"""
		Scans all liveries for a certain "Mod".

		:param path: A path to a "Mod", e.g. "CoreMods", custom "Mods" in saved games, etc.
		"""
		if os.path.exists(path):
			for unit in os.listdir(path):
				liveries_path = os.path.join(path, unit, "Liveries")
				if os.path.exists(liveries_path):
					Liveries.scan_liveries(liveries_path)

	@staticmethod
	def scan_dcs_installation():
		"""
		Scans all liveries in DCS' installation folder
		"""
		root = get_dcs_install_directory()

		path1 = os.path.join(root, "CoreMods", "aircraft")
		path2 = os.path.join(root, "CoreMods", "WWII Units")
		path3 = os.path.join(root, "Bazar", "Liveries")

		Liveries.scan_mods_path(path1)
		Liveries.scan_mods_path(path2)
		Liveries.scan_liveries(path3)

	@staticmethod
	def scan_custom_liveries():
		"""
		Scans all custom liveries & liveries of aircraft mods.
		"""
		root = get_dcs_saved_games_directory()

		path1 = os.path.join(root, "Liveries")
		path2 = os.path.join(root, "Mods", "aircraft")

		Liveries.scan_liveries(path1)
		Liveries.scan_mods_path(path2)


Liveries()  # initialization


if __name__ == "__main__":
	from planes import FA_18C_hornet
	f18 = FA_18C_hornet()
	print(f18.livery_name, f18.Liveries)

	from helicopters import AH_64D_BLK_II
	ah64 = AH_64D_BLK_II()
	print(ah64.livery_name, ah64.Liveries)

	# skins = Liveries()
	# for u in skins:
	# 	print(u)
	# 	for liv in skins[u]:
	# 		print("\t", liv)
	# 		if skins[u][liv] is None:
	# 			print("\t\t All countries")
	# 			continue
	# 		print("\t\t", skins[u][liv])
