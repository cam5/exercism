--- square the sum of natural numbers up to and including n
-- @param n The natural number
-- @return sthe
local function square_of_sum(n)
  numbers = {}

  for i = 1, n do
    numbers[i] = i
  end

  local acc = 0

  for i, val in ipairs(numbers) do
    acc = acc + val
  end

  return acc * acc
end

local function sum_of_squares(n)
  squares = {}

  for i = 1, n do
    squares[i] = i * i
  end

  local acc = 0

  for i, val in ipairs(squares) do
    acc = acc + val
  end

  return acc
end

local function difference_of_squares(n)
  return square_of_sum(n) - sum_of_squares(n)
end

return {
  square_of_sum = square_of_sum,
  sum_of_squares = sum_of_squares,
  difference_of_squares = difference_of_squares
}
