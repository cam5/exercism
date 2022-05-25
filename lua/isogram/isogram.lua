return function(s)
  t = {}
  isogram = true

  for str in string.gmatch(s:lower(), ".") do
    if (t[str] ~= nil) then
      isogram = false
    end

    table.insert(t, str)
  end

  return isogram
end
