def solve(signal, table)
  result = ''

  while not signal.empty?
    match = table.find do |code, letter|
      signal.start_with? code
    end

    return 'ONMOGELIJK' unless match

    code, letter = match
    signal = signal[code.size..-1]
    result += letter
  end

  result
end

def main
  (1..gets.to_i).each do |index|
    signal = gets.strip

    table = []
    (1..gets.to_i).map do
      letter = gets.strip
      code  = gets.strip
      table << [ code, letter ]
    end
    table.sort_by! { |code, letter| -code.size }

    solution = solve(signal, table)

    puts "#{index} #{solution}"
  end
end

main