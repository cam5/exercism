local house = {}

subjects = {
  { subject = 'Jack' },
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
  if which == 1 then
    return 'This is the house that Jack built.'
  end
end

house.recite = function()
  all = {}

  for i = 2, (#subjects + 1) do
    table.insert(
      all,
      string.format(
        '%s that %s the %s',
        subjects[i].subject,
        subjects[i].action,
        (subjects[i - 1]) and (subjects[i - 1].subject) or 'Jack'
      )
    )
  end

  return table.concat(all, '\n')
end

return house
