#!/usr/bin/env ruby
# 1. Repetition Token #0

puts ARGV[0].scan(/hb[A-Z]{2,5}n/i).join
