import os
import re
import zipfile

from dcs.installation import get_dcs_install_directory, get_dcs_saved_games_directory
from typing import Optional, Dict

liveries_map: Dict[str, Dict[str, set[str] | None]] = {}
"""
A dictionary containing all liveries for each unit.
Mind that the unit uses the name of the livery folder, and not the ID.
Every livery has a set of countries for which the livery is applicable.
In case countries is None, it indicates the livery is valid for all countries

Unit (str) -> {Livery (str) -> CountrySet (set[str]) | None}
"""


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
	if livery_name in liveries_map[unit]:
		if country is not None:
			liveries_map[unit][livery_name].add(country)
	else:
		liveries_map[unit][livery_name] = country if country is None else {country}


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
			add_or_append(unit, livery_name, country)
	else:
		add_or_append(unit, livery_name)


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
			scan_lua_code(code, path, unit)


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
					scan_lua_code(code, path, unit)


def scan_liveries(path: str) -> None:
	"""
	Scans liveries for all units in the given path.

	:param path: A 'Liveries' path containing one or more units
	"""
	for unit in os.listdir(path):
		# The unit's name for liveries (i.e. the 'DCS type') is NOT case-sensitive
		# thus convert 'unit' to upper/lower to make sure everything "merges properly"
		unit = unit.upper()
		if "COCKPIT" in unit:
			# Some custom mods put their cockpit liveries in the same directory,
			# for the time being we don't want to load those...
			continue
		if unit not in liveries_map:
			liveries_map[unit.upper()] = {}
		liveries_path = os.path.join(path, unit)
		for livery in os.listdir(liveries_path):
			livery_path = os.path.join(liveries_path, livery)
			if os.path.isdir(livery_path):
				scan_lua_description(livery_path, unit)
			elif os.path.isfile(livery_path) and ".zip" in livery_path:
				scan_zip_file(livery_path, unit)


def scan_mods_path(path: str) -> None:
	"""
	Scans all liveries for a certain "Mod".

	:param path: A path to a "Mod", e.g. "CoreMods", custom "Mods" in saved games, etc.
	"""
	if os.path.exists(path):
		for unit in os.listdir(path):
			liveries_path = os.path.join(path, unit, "Liveries")
			if os.path.exists(liveries_path):
				scan_liveries(liveries_path)


def scan_dcs_installation():
	"""
	Scans all liveries in DCS' installation folder
	"""
	root = get_dcs_install_directory()

	path1 = os.path.join(root, "CoreMods", "aircraft")
	path2 = os.path.join(root, "CoreMods", "WWII Units")
	path3 = os.path.join(root, "Bazar", "Liveries")

	scan_mods_path(path1)
	scan_mods_path(path2)
	scan_liveries(path3)


def scan_custom_liveries():
	"""
	Scans all custom liveries & liveries of aircraft mods.
	"""
	root = get_dcs_saved_games_directory()

	path1 = os.path.join(root, "Liveries")
	path2 = os.path.join(root, "Mods", "aircraft")

	scan_liveries(path1)
	scan_mods_path(path2)


scan_dcs_installation()
scan_custom_liveries()


if __name__ == "__main__":
	from planes import FA_18C_hornet
	f18 = FA_18C_hornet()
	print(f18.Liveries)
	# for u in liveries_map:
	# 	print(u)
	# 	for liv in liveries_map[u]:
	# 		print("\t", liv)
	# 		if liveries_map[u][liv] is None:
	# 			print("\t\t All countries")
	# 			continue
	# 		print("\t\t", liveries_map[u][liv])
	# 		for c in liveries_map[u][liv]:
	# 			print("\t\t", c)
