--[[
  We want to have whatever is exported have a function that returns a class
  instance. `m = Matrix(i)` `m.row(n)` etc. etc.

  However, as per @link {http://lua-users.org/wiki/ObjectOrientationTutorial}
  lua doesn't have a built-in concept of "Classes".

  But we can have the top level function from this module export a table with
  methods & data instantiated by the "constructor".
--]]

Matrix = {}
Matrix_mt = { __index = Matrix }

local self = setmetatable({ __index = Matrix }, Matrix)

function Matrix:new(i)
  matrix = setmetatable({}, Matrix_mt)

  rows = {}

  for row in i:gmatch("%C+") do
    numbers = {}
    for num in row:gmatch("%S+") do
      table.insert(numbers, (num + 0))
    end

    table.insert(rows, numbers)
  end

  matrix.rows = rows

  return matrix;
end

return function(i)
  matrix = Matrix:new(i)

  matrix.row = function(i)
    return matrix.rows[i]
  end

  return matrix
end
