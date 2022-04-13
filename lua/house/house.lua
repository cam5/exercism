local house = {}

subjects = {
  { subject = 'house', action = 'built' },
  { subject = 'malt', action = 'lay in' },
  { subject = 'rat', action = 'ate' },
  { subject = 'cat', action = 'killed' },
  { subject = 'dog', action = 'worried' },
  { subject = 'cow with the crumpled horn', action = 'tossed' },
  { subject = 'maiden all forlorn', action = 'milked' },
  { subject = 'man all tattered and torn', action = 'kissed' },
  { subject = 'priest all shaven and shorn', action = 'married' },
  { subject = 'rooster that crowed in the morn', action = 'woke' },
  { subject = 'farmer sowing his corn', action = 'kept' },
  { subject = 'horse and the hound and the horn', action = 'belonged to' }
}

house.verse = function(which)
  local all = {}

  for iteration = 1, which do
    local index = (which - iteration + 1)

    local action = subjects[index].action
    local subject = subjects[index].subject
    local target = (subjects[index - 1]) and (subjects[index - 1].subject) or 'Jack'

    local secondArg = (iteration == 1 and target or action)
    local thirdArg = (iteration == 1 and action or target)

    table.insert(
      all,
      string.format(
        'the %s that %s %s',
        subject,
        secondArg,
        thirdArg
      )
    )
  end

  return 'This is ' .. table.concat(all, '\n') .. '.'
end

house.recite = function()
  return ''
end

return house
