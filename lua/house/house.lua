local house = {}

lines = {
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

house.verse = function(verseNumber)
  local verse = ''

  -- arrays/tables are 1-indexed in lua
  for iteration = 1, verseNumber do
    local targetLine = (verseNumber - iteration + 1)
    local verseObjects = lines[targetLine]

    if iteration == 1 then
      verse = 'This is the ' .. lines[verseNumber].subject
    end

    if iteration < verseNumber then
      verse = verse .. '\nthat ' .. verseObjects.action .. ' the ' .. lines[targetLine - 1].subject
    else
      verse = verse .. ' that Jack ' .. lines[targetLine].action .. '.'
    end
  end

  return verse
end

house.recite = function()
  local verses = {}

  for i = 1, #lines do
    table.insert(verses, house.verse(i))
  end

  return table.concat(verses, '\n')
end

return house
