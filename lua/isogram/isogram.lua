function printtable(table, indent)
  print(tostring(table) .. '\n')
  for index, value in pairs(table) do
    print('    ' .. tostring(index) .. ' : ' .. tostring(value) .. '\n')
  end
end

return function(s)
  t = {}
  isogram = true
  s = s:lower()

  for str in string.gmatch(s, ".") do
    if (table.concat(t):find(str)) then
      isogram = false
    end

    table.insert(t, str)
  end

  return isogram
end
