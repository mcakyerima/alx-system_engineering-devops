#!/usr/bin/env ruby
# a regex that parses a logfile and output [sender],[receiver],[flags]

puts ARGV[0].scan(/\[(?:from:|to:|flags:)(.*?)\]/).join(",")
