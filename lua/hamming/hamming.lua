local Hamming = {}

function Hamming.compute(a, b)
  -- disallow different length of strands
  if string.len(a) ~= string.len(b) then
    return -1
  end

  ham_distance = 0

  for i = 1, string.len(a) do
    if string.sub(a, i, i) ~= string.sub(b, i, i) then
      ham_distance = ham_distance + 1
    end
  end

  return ham_distance
end

return Hamming
