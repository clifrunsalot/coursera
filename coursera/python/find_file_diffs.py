"""
Project for Week 4 of "Python Data Representations".
Find differences in file contents.

This module contains the methods required for compares two files
and returns the first difference discovered if any.

"""

IDENTICAL = -1

def singleline_diff(line1, line2):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
    Output:
      Returns the index where the first difference between
      line1 and line2 occurs.

      Returns IDENTICAL if the two lines are the same.
    """

    # Loop thru the index of smaller string to avoid OUT_OF_BOUNDS
    # error.
    #
    # If the strings are of unequal length and the shorter string
    # is a subset of the longer string, starting from 0 to the end
    # of the shorter string, then the diff occurs at the index
    # of the end of the shorter string plus 1.

    diff_idx = IDENTICAL
    len_line1 = len(line1)
    len_line2 = len(line2)
    dummy_ch1 = -1

    if len_line1 < len_line2:
        for dummy_ch1 in range(len_line1):
            if line1[dummy_ch1] != line2[dummy_ch1]:
                diff_idx = dummy_ch1
                break
        if diff_idx == IDENTICAL:
            if len_line1 == 0:
                diff_idx = 0
            else:
                diff_idx = dummy_ch1 + 1

    elif len_line1 > len_line2:
        for dummy_ch1 in range(len_line2):
            if line1[dummy_ch1] != line2[dummy_ch1]:
                diff_idx = dummy_ch1
                break
        if diff_idx == IDENTICAL:
            if len_line1 == 0:
                diff_idx = 0
            else:
                diff_idx = dummy_ch1 + 1

    else:
        for dummy_ch1 in range(len_line1):
            if line1[dummy_ch1] != line2[dummy_ch1]:
                diff_idx = dummy_ch1
                break

    return diff_idx

def singleline_diff_format(line1, line2, idx):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
      idx   - index of first difference between the lines
    Output:
      Returns a three line formatted string showing the location
      of the first difference between line1 and line2.

      If either input line contains a newline or carriage return,
      then returns an empty string.

      If idx is not a valid index, then returns an empty string.
    """
    valid = False
    ret_val = ""
    last_idx_line1 = len(line1) - 1
    last_idx_line2 = len(line2) - 1
    # idx must be <= 1 + last_idx of shortest line.
    if idx == -1:
        valid = False
    elif idx == 0:
        valid = True
    else:
        if last_idx_line1 < last_idx_line2:
            if idx <= (last_idx_line1 + 1):
                valid = True
        elif last_idx_line2 < last_idx_line1:
            if idx <= (last_idx_line2 + 1):
                valid = True
        else:
            if idx <= last_idx_line1:
                valid = True
            elif idx == 0:
                valid = True

    if valid:
        # Make sure that there are no line returns.
        if not "\n" in line1 and not "\r" in line1 \
            and not "\n" in line2 and not "\r" in line2:
            ret_val = line1 + '\n'
            ret_val = ret_val + ("=" * idx) + "^" + '\n'
            ret_val = ret_val + line2 + '\n'
    return ret_val

def multiline_diff(lines1, lines2):
    """
    Inputs:
      lines1 - list of single line strings
      lines2 - list of single line strings
    Output:
      Returns a tuple containing the line number (starting from 0) and
      the index in that line where the first difference between lines1
      and lines2 occurs.

      Returns (IDENTICAL, IDENTICAL) if the two lists are the same.
    """

    len_lst1 = len(lines1)
    len_lst2 = len(lines2)
    diff_idx = IDENTICAL
    diff_tup = (IDENTICAL, IDENTICAL)
    l_idx = -1

    # loop thru the larger of the two strings to avoid OUT_OF_BOUNDS
    # error. Does not assume the lists are of equal length.
    if len_lst1 < len_lst2:
        for l_idx in range(len(lines1)):
            ln1 = lines1[l_idx]
            ln2 = lines2[l_idx]
            diff_idx = singleline_diff(ln1, ln2)
            if diff_idx > -1:
                diff_tup = (l_idx, diff_idx)
                break
        if diff_idx == -1:
            diff_tup = (l_idx + 1, 0)

    elif len_lst1 > len_lst2:
        for l_idx in range(len(lines2)):
            ln1 = lines1[l_idx]
            ln2 = lines2[l_idx]
            diff_idx = singleline_diff(ln1, ln2)
            if diff_idx > -1:
                diff_tup = (l_idx, diff_idx)
                break
        if diff_idx == -1:
            diff_tup = (l_idx + 1, 0)

    else:
        for l_idx in range(len(lines2)):
            ln1 = lines1[l_idx]
            ln2 = lines2[l_idx]
            diff_idx = singleline_diff(ln1, ln2)
            if diff_idx > -1:
                diff_tup = (l_idx, diff_idx)
                break

    return diff_tup

def get_file_lines(filename):
    """
    Inputs:
      filename - name of file to read
    Output:
      Returns a list of lines from the file named filename.  Each
      line will be a single line string with no newline ('\n') or
      return ('\r') characters.

      If the file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    data = []
    in_file = open(filename, 'rt')
    file_contents = list(in_file)
    in_file.close()
    for ln1 in file_contents:
        ln1 = ln1.replace('\n', '')
        ln1 = ln1.replace('\r', '')
        data.append(ln1)
    return data

def file_diff_format(filename1, filename2):
    """
    Inputs:
      filename1 - name of first file
      filename2 - name of second file
    Output:
      Returns a four line string showing the location of the first
      difference between the two files named by the inputs.

      If the files are identical, the function instead returns the
      string "No differences\n".

      If either file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    diff_idx = IDENTICAL
    ret_val = "No differences\n"
    content1 = get_file_lines(filename1)
    content2 = get_file_lines(filename2)

    diff_tup = multiline_diff(content1, content2)
    if diff_tup == (-1, -1):
        ret_val = "No differences\n"
    else:

        c1i = 0
        len_cnt1 = len(content1)
        len_cnt2 = len(content2)

        # Does not assume the list lengths are the same.
        if len(content1) < len(content2):
            if len_cnt1 > 0:
                for c1i in range(len(content1)):
                    str1 = content1[c1i]
                    str2 = content2[c1i]
                    diff_idx = singleline_diff(str1, str2)
                    if diff_idx > -1:
                        ret_val = "Line {}:".format(c1i) + '\n'
                        ret_val = ret_val + singleline_diff_format(str1, str2, diff_idx)
                        break
            else:
                str1 = ''
                str2 = content2[0]
                ret_val = "Line {}:".format(0) + '\n'
                ret_val = ret_val + singleline_diff_format(str1, str2, 0)

        elif len(content1) > len(content2):
            if len_cnt2 > 0:
                for c1i in range(len(content2)):
                    str1 = content1[c1i]
                    str2 = content2[c1i]
                    diff_idx = singleline_diff(str1, str2)
                    if diff_idx > -1:
                        ret_val = "Line {}:".format(c1i) + '\n'
                        ret_val = ret_val + singleline_diff_format(str1, str2, diff_idx)
                        break
            else:
                str1 = content1[0]
                str2 = ''
                ret_val = "Line {}:".format(0) + '\n'
                ret_val = ret_val + singleline_diff_format(str1, str2, 0)

        else:
            if len_cnt1 > 0:
                for c1i in range(len(content2)):
                    str1 = content1[c1i]
                    str2 = content2[c1i]
                    diff_idx = singleline_diff(str1, str2)
                    if diff_idx > -1:
                        ret_val = "Line {}:".format(c1i) + '\n'
                        ret_val = ret_val + singleline_diff_format(str1, str2, diff_idx)
                        break

    return ret_val



##
## Tests for singleline_diff
##
## line2 is longer.
#ln1 = "Hello, my name is George"
#ln2 = "Hello, my name is George Hanson"
#idx = singleline_diff(ln1, ln2)
#print(ln1)
#print(("=" * idx) + "^")
#print(ln2)
#print()

## line1 is longer and line2 is different.
#ln1 = "Hello, my name is George Hanson"
#ln2 = "Hello, my name is george"
#idx = singleline_diff(ln1, ln2)
#print(ln1)
#print(("=" * idx) + "^")
#print(ln2)
#print()

## line1 == line2
#ln1 = "Hello, my name is George"
#ln2 = "Hola, my name is George"
#idx = singleline_diff(ln1, ln2)
#print(ln1)
#print(("=" * idx) + "^")
#print(ln2)
#print()

#print(singleline_diff('','a'))
#print(singleline_diff('abc',''))



#
# singleline_diff_format
#

#ln1 = "Hello, my name is George"
#ln2 = "Hola, my name is George."
#diff_idx = singleline_diff(ln1, ln2)
#print(singleline_diff_format(ln1,ln2,diff_idx))

#ln1 = "Hello, my name is George Hanson"
#ln2 = "Hello, my name is George"
#diff_idx = singleline_diff(ln1, ln2)
#print(singleline_diff_format(ln1,ln2,diff_idx))

#ln1 = "Hello, my name is Jeorge"
#ln2 = "Hello, my name is George"
#diff_idx = singleline_diff(ln1, ln2)
#print(singleline_diff_format(ln1,ln2,diff_idx))

#ln1 = "Hello, my name is George"
#ln2 = "Hello, my name is George"
#diff_idx = singleline_diff(ln1, ln2)
#print(singleline_diff_format(ln1,ln2,diff_idx))

#ln1 = "Hello, my name is Jeorge\n"
#ln2 = "Hello, my name is George"
#diff_idx = singleline_diff(ln1, ln2)
#print(singleline_diff_format(ln1,ln2,diff_idx))

#ln1 = "Hello, my name is Jeorge\r"
#ln2 = "Hello, my name is George"
#diff_idx = singleline_diff(ln1, ln2)
#print(singleline_diff_format(ln1,ln2,diff_idx))

#print(singleline_diff_format('abcdefg', 'abc', 5))
#print(singleline_diff_format('bc', 'abc', 0))
#print(singleline_diff_format('abc', 'abd', 2))
#print(singleline_diff_format('', '', 0))
print(singleline_diff_format('abc', '', 0))


#
# multiline_diff
#

#lines1 = ["Hello, my name is George","Hello, my name is Mike","Hello, my name is Jeorge"]
#lines2 = ["Hola, my name is Gorge","Hello, my name is Mike","Hello, my name is Jeorge"]
#print(multiline_diff(lines1, lines2))

#lines1 = ["Hello, my name is George","Hello, my name is Mike","Hello, my name is Jeorge"]
#lines2 = ["Hello, my name is George","Hello, my Name is Mike","Hello, my name is Jeorge"]
#print(multiline_diff(lines1, lines2))

#lines1 = ["Hello, my name is George","Hello, my name is Mike","Hello, my name is Jeorge"]
#lines2 = ["Hello, my name is George","Hello, my name is Mike","Hello, my name is George"]
#print(multiline_diff(lines1, lines2))

#lines1 = ["Hello, my name is George","Hello, my name is Mike","Hello, my name is Jeorge"]
#lines2 = ["Hello, my name is George","Hello, my name is Mike","Hello, my name is Jeorge"]
#print(multiline_diff(lines1, lines2))

#lines1 = ["line1","line2"]
#lines2 = ["line1","line2","line3"]
#print(multiline_diff(lines1, lines2))

#lines1 = []
#lines2 = ["line1"]
#print(multiline_diff(lines1, lines2))


#
# get_file_lines
#
#content = []
#content = get_file_lines('file_1.txt')
#print(content)
#content = get_file_lines('file_2.txt')
#print(content)
#content = get_file_lines('file_3.txt')
#print(content)

#
# file_diff_format
#
FILE1 = 'isp_diff_files/file8.txt'
FILE2 = 'isp_diff_files/file9.txt'
#FILE3 = 'file_3.txt'
print(file_diff_format(FILE1, FILE2))
#print(file_diff_format(FILE2, FILE3))
#print(file_diff_format(FILE1, FILE3))
