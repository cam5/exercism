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

    table.insert(
      all,
      string.format(
        '%s that %s',
        subject,
        target
      )
    )
  end

  return 'This is the ' .. table.concat(all, '\n') .. ' built.'
end

house.recite = function()
  return ''
end

return house
