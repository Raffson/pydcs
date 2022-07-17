import os
import re
import zipfile

from dcs.installation import get_dcs_install_directory, get_dcs_saved_games_directory
from typing import Optional, Dict, Iterator, Set


def regex_group_extractor(regex: str, text: str, fallback=None):
	match = re.search(regex, text, re.MULTILINE)
	if match is not None:
		return match.group(1)
	else:
		return fallback


class Livery:
	id: str = ""
	"""ID of the livery, corresponds with the folder-name of the livery."""

	name: str = ""
	"""Name of the livery"""

	order: int = 0
	"""Order of the livery used to sort like DCS"""

	countries: set[str] | None = None
	"""Set of short names indicating valid countries, with 'None' indicating all countries."""

	def __init__(self, path_id: str, name: str, order: int, countries: Optional[Set[str]]) -> None:
		self.id = path_id
		self.name = name
		self.order = order
		self.countries = countries

	def __str__(self) -> str:
		return self.name

	def __repr__(self) -> str:
		return self.name

	def __lt__(self, other):
		if self.order == other.order:
			return self.name < other.name
		if self.order is None:
			return True
		return False if other.order is None else self.order < other.order


class Liveries:
	"""
	Class containing a map of all units with their respective liveries.
	Each livery has a set of countries to indicate applicability
	"""

	map: Dict[str, Set[Livery]] = {}
	"""
	A dictionary containing all liveries for each unit.
	Mind that the unit uses the name of the livery folder, and not the ID.
	Every livery has a set of countries for which the livery is applicable.
	In case countries is None, it indicates the livery is valid for all countries

	Unit (str) -> {Livery (str) -> CountrySet (set[str]) | None}
	"""

	def __init__(self) -> None:
		"""
		Constructor only attempts to initialize if 'map' is empty.
		You can also initialize manually by calling 'Liveries.initialize'.
		"""
		if len(Liveries.map) == 0:
			Liveries.initialize()

	def __getitem__(self, unit: str) -> Set[Livery]:
		liveries = Liveries.map.get(unit)
		return liveries if liveries is not None else set()

	def __setitem__(self, unit: str, liveries: Set[Livery]) -> None:
		if unit in Liveries.map:
			Liveries.map[unit].update(liveries)
		else:
			Liveries.map[unit] = liveries

	def __delitem__(self, unit: str) -> None:
		del Liveries.map[unit]

	def __iter__(self) -> Iterator[str]:
		return Liveries.map.__iter__()

	@staticmethod
	def initialize(install: str = "", saved_games: str = "") -> None:
		"""
		Initializes the Liveries map given the root install directory for DCS
		and the path to its Saved Games folder.

		:param install: Path to DCS' installation folder,
			if empty PyDCS will attempt to determine this.
		:param saved_games: Path to the Saved Games folder,
			if empty PyDCS will attempt to determine this.
		"""
		Liveries.map.clear()
		Liveries.scan_dcs_installation(install)
		Liveries.scan_custom_liveries(saved_games)

	@staticmethod
	def scan_lua_code(luacode: str, path: str, unit: str) -> None:
		"""
		Scans the given code (expecting contents from a description.lua file)
		to extract the name of the livery together with the countries for which the livery is applicable.
		If no name is found, it defaults to the folder-name like DCS would.
		If no countries are found, it means the livery is valid for all countries.
		Finally we also attempt to extract the order to sort liveries like DCS.
		If no order is found, we use a default value of 0.

		:param luacode: The contents of description.lua for the livery in question
		:param path: The path of the livery in question
		:param unit: The name of the unit as 'DCS type',
			i.e. name of the unit inside the Liveries folder, e.g. 'A-10CII'
		"""
		path_id = path.split('\\')[-1].replace(".zip", "")
		if path_id == "placeholder":
			return
		livery_name = regex_group_extractor(r'^name\s*=\s*"(.*)"\s*(?:--.*)?$', luacode, path_id)

		regex = r'^countries\s*=\s*(\{["[A-Z]+"\s*]?(?:,\s*"[A-Z]+"\s*)*\s*,?\s*\})\s*(?:--.*)?$'
		countries = regex_group_extractor(regex, luacode)
		if countries is not None:
			exec(f"country_list = {countries}")
			countries = set(filter(lambda x: x != "", locals()['country_list']))

		order = regex_group_extractor(r'^order\s*=\s*(-?[0-9]+)\s*(?:--.*)?$', luacode, 0)
		if not isinstance(order, int):
			try:
				order = int(order)
			except ValueError:
				order = 0
		order = None if path_id == "default" else order
		
		livery = Livery(path_id, livery_name, order, countries)
		Liveries()[unit] = {livery}

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
		if not os.path.exists(path):
			return
		for unit in os.listdir(path):
			# The unit's name for liveries is NOT case-sensitive
			# thus convert 'unit' to upper/lower to make sure everything "merges properly"
			unit = unit.upper()
			if "COCKPIT" in unit:
				# Some custom mods put their cockpit liveries in the same directory,
				# for the time being we don't want to load those...
				continue
			liveries_path = os.path.join(path, unit)
			if not os.path.isdir(liveries_path):
				continue
			if unit not in Liveries.map:
				Liveries.map[unit.upper()] = set()
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
		if not os.path.exists(path):
			return
		for unit in os.listdir(path):
			liveries_path = os.path.join(path, unit, "Liveries")
			if os.path.exists(liveries_path):
				Liveries.scan_liveries(liveries_path)

	@staticmethod
	def scan_campaign_liveries(path: str) -> None:
		"""
		Scans all extra liveries from campaigns.

		:param path: The path to 'DCS-installation/Mods/campaigns'.
		"""
		if not os.path.exists(path):
			return
		for campaign in os.listdir(path):
			liveries_path = os.path.join(path, campaign, "Liveries")
			if os.path.exists(liveries_path):
				Liveries.scan_liveries(liveries_path)

	@staticmethod
	def scan_dcs_installation(install: str = ""):
		"""
		Scans all liveries in DCS' installation folder

		:param install: Path to DCS' installation folder,
			if an empty string or invalid path was given PyDCS will attempt to determine this.
		"""
		root = install
		if root == "" or not os.path.isdir(root):
			root = get_dcs_install_directory()

		path1 = os.path.join(root, "CoreMods", "aircraft")
		path2 = os.path.join(root, "CoreMods", "WWII Units")
		path3 = os.path.join(root, "Bazar", "Liveries")
		path4 = os.path.join(root, "Mods", "campaigns")
		path5 = os.path.join(root, "CoreMods", "tech")

		Liveries.scan_mods_path(path1)
		Liveries.scan_mods_path(path2)
		Liveries.scan_liveries(path3)
		Liveries.scan_campaign_liveries(path4)
		Liveries.scan_mods_path(path5)

	@staticmethod
	def scan_custom_liveries(saved_games: str = ""):
		"""
		Scans all custom liveries & liveries of aircraft mods.

		:param saved_games: Path to Saved Games folder,
			if an empty string or invalid path was given PyDCS will attempt to determine this.
		"""
		root = saved_games
		if root == "" or not os.path.isdir(root):
			root = get_dcs_saved_games_directory()

		path1 = os.path.join(root, "Liveries")
		path2 = os.path.join(root, "Mods", "aircraft")

		Liveries.scan_liveries(path1)
		Liveries.scan_mods_path(path2)


if __name__ == "__main__":
	from planes import FA_18C_hornet, F_16C_50, F_14B, F_15E, A_10C_2
	# for some reason 'Liveries' in the current scope is a different object
	f18 = FA_18C_hornet()
	print(f18.livery_name, sorted(f18.Liveries))
	print(f18.default_livery("CAN"))
	print(f18.default_livery("ISR"))
	print(f18.default_livery("USA"))

	f14 = F_14B()
	print(f14.livery_name, sorted(f14.Liveries))
	print(f14.default_livery("USA"))
	print(f14.default_livery("IRN"))
	print(f14.default_livery("GRC"))
	print(f14.default_livery("POL"))

	f15 = F_15E()
	print(f15.livery_name, sorted(f15.Liveries))
	print(f15.default_livery("USA"))
	print(f15.default_livery("ISR"))
	print(f15.default_livery("GRC"))
	print(f15.default_livery("POL"))

	a10c2 = A_10C_2()
	print(a10c2.livery_name, sorted(a10c2.Liveries))
	print(a10c2.default_livery("USA"))
	print(a10c2.default_livery("ISR"))
	print(a10c2.default_livery("GRC"))
	print(a10c2.default_livery("POL"))

	f16 = F_16C_50()
	print(f16.livery_name, sorted(f16.Liveries))
	print(f16.default_livery("USA"))
	print(f16.default_livery("ISR"))
	print(f16.default_livery("GRC"))
	print(f16.default_livery("POL"))

	from helicopters import AH_64D_BLK_II
	ah64 = AH_64D_BLK_II()
	print(ah64.livery_name, sorted(ah64.Liveries))
	print(ah64.default_livery("USA"))
	print(ah64.default_livery("ISR"))

	# skins = Liveries()
	# for u in skins:
	# 	print(u)
	# 	for liv in sorted(skins[u]):
	# 		print("\t", liv, liv.countries)
