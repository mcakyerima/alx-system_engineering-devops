#!/usr/bin/env ruby
# A regex that matches a string that starts with "h" and ends with "n" with single char

puts ARGV[0].scan(/h.n/).join
