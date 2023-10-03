#!/usr/bin/env ruby
# a regex that matches "hbtn & htn" ! "hbbtn"

puts ARGV[0].scan(/hb?tn/).join
