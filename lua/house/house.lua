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
  -- "scope" in lua works differently than I expected!
  -- global by default, and `local` keyword only makes it scoped to a block
  -- https://www.lua.org/pil/4.2.html
  local all = {
    'This is the ' .. lines[verseNumber].subject,
  }

  -- arrays/tables are 1-indexed in lua
  for iteration = 1, verseNumber do
    local targetLine = (verseNumber - iteration + 1)
    local verseObjects = lines[targetLine]

    print(targetLine)

    if iteration > verseNumber then
      table.insert(
        all,
        'that ' .. verseObjects.action .. ' the ' .. lines[targetLine].subject
      )
    else
      table.insert(all, 'that Jack ' .. verseObjects.action .. '.')
    end
  end

  local glueChar = '\n'

  if verseNumber == 1 then
    glueChar = ' '
  end

  return table.concat(all, glueChar)
end

house.recite = function()
  return ''
end

return house
