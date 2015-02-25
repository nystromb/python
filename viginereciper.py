#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  viginereciper.py

import sys

en_ciper = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",",",".","-","_"]

def main():
  
  if sys.argv == 1: 
    print "Please enter a valid message"
    print "USAGE: python pythonscript.py message_to_encrypt"
    quit()
  if sys.argv > 1:
    plntxt_input = sys.argv[1]
    
  key_input = raw_input("Enter Key: ")
  
  plntxt = plntxt_input.lower()
  key = key_input.lower()
  
  
  if len(key) <= len(plntxt):
    full_blocks = len(plntxt)/len(key) 
    rem_blocks = len(plntxt)%len(key)
  else:
	full_blocks = 1
	rem_blocks = 0
    
  ciphertext = encrypt(key, plntxt, full_blocks, rem_blocks)
  print "Ciphertext: " + ciphertext.upper()

  return 0

def encrypt(k, p, blocks, remaining):
  block_count = 0
  key_length = len(k)
  next_block = ""

  #cycle through full blocks
  while block_count < blocks:
    for letter in range(block_count*key_length, ((block_count+1)*key_length), 1):
      #find new index, and insert letter on the block
	  new_index = en_ciper.index(p[letter]) + en_ciper.index(k[letter])
	  next_block += en_ciper[new_index%30]
    #append next block to the key when done with block
    k += next_block
    next_block = ""
    block_count = block_count + 1
  
  #check for remainder block
  if remaining > 0:
    for letter in range(blocks*key_length, len(p), 1):
      new_index = en_ciper.index(p[letter]) + en_ciper.index(k[letter])
      next_block += en_ciper[new_index%30]

  k += next_block
  next_block = ""

  return k[key_length:]
  
	  
	  
if __name__ == '__main__':
   main()

