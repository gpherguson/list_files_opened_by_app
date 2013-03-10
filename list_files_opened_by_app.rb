FILENAME = 'trashme.txt'

pid  = $$
lsof = []

File.open(FILENAME, 'w') do |fo|
  fo.puts 'This is a test'

  IO.popen ("lsof -p #{pid}") { |l| lsof << l.readlines }

end
puts lsof.select{ |i| i[FILENAME] }
