#!/usr/bin/env ruby
# A regex that matches "hbn, hbtn, hbtttttn" but not "hbon"

puts ARGV[0].scan(/hbt*n/).join
