#!/usr/bin/env ruby
# a regex that matches "hbtn, hbttn, hbtttn, hbttttn" not "hbn"

puts ARGV[0].scan(/hbt+n/).join
