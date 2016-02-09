-- to create the weapons.lua:
-- make sure all files are correctly converted from Cyrilic(Windows 1251) encoding to UTF-8
-- copy wsTypes.lua into weapons.lua
-- attach db_weapons.lua on weapons.lua
-- add a newline to weapons.lua
-- attach db_weapons_data.lua to weapons.lua
-- remove the dofile call in weapons.lua

function _(s)
	return s
end

db = {}
dofile('weapons.lua')

print("# Don't change this file, it's generated.")
print("class Weapons:")
weapons = {}
keys = {}
for j in pairs({1,2,3,4,5}) do
	for i, v in ipairs(db.Weapons.Categories[j].Launchers) do
		local pyName = v.displayName
		if string.sub(v.CLSID, 0, 1) ~= "{" then
			pyName = v.CLSID
		end
		pyName = string.gsub(pyName, "[-()/., *']", "_")
		pyName = string.gsub(pyName,"^([0-9])", "_%1")
		key = pyName
		if weapons[key] ~= nil then
			key = pyName .. "_"
		end
		local w = "None"
		if v["Weight"] ~= nil then
			w = v["Weight"]
		end
		weapons[key] = {clsid = v.CLSID, displayName = v.displayName, weight = w}
		table.insert(keys, key)
		-- print("    " .. key .. " = {\"clsid\": \"" .. v.CLSID .. "\", \"name\": \"" .. v.displayName .. "\"}")
	end
end

table.sort( keys )
local i = 1
while i < #keys do
	local x = keys[i]
	print("    " .. x .. " = {\"clsid\": \"" .. weapons[x].clsid
		.. "\", \"name\": \"" .. weapons[x].displayName .. "\", \"weight\": " .. weapons[x].weight .. "}")
	i = i + 1
end

print()
print("weapon_ids = {")
i = 1
while i < #keys do
	local x = keys[i]
	local s = "    \"" .. weapons[x].clsid .. "\" : Weapons." .. x
	i = i + 1
	if i < #keys then
		s = s .. ","
	end
	print(s)
end
print("}")
