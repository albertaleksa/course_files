import re

# find first match using compile pattern before
pattern = re.compile(r'\d{3} \d{3}-\d{4}')
res1 = pattern.search("call me at 310 456-1234 or 132 789-4562")
print(res1.group())

# find first match without using compile pattern before
res2 = re.search(r'\d{3} \d{3}-\d{4}', "call me at 310 456-1234 or 132 789-4562")
print(res2.group())

# find all matches using compile pattern before
res3 = pattern.findall("call me at 310 456-1234 or 132 789-4562")
print(res3)

# find all matches without using compile pattern before
res4 = re.findall(r'\d{3} \d{3}-\d{4}', "call me at 310 456-1234 or 132 789-4562")
print(res4)

print("----------------------------")


# extract first phone number from string
def extract_phone(input):
    phone_regex = re.compile(r'\b\d{3} \d{3}-\d{4}\b')
    match = phone_regex.search(input)
    if match:
        return match.group()
    return None


print(extract_phone("my number is 132 789-4562"))
print(extract_phone("my number is 132 789-456278"))
print(extract_phone("132 789-4562 dffgfg "))
print(extract_phone("132 789-4562"))


# extract all phone numbers from string
def extract_all_phones(input):
    phone_regex = re.compile(r'\b\d{3} \d{3}-\d{4}\b')
    return phone_regex.findall(input)


print(extract_all_phones("my number is 132 789-4562 or call me at 456 789-9638"))
print(extract_all_phones("my number is 132 789-456"))


# check if entire string is a phone number
def is_valid_phone(input):
    phone_regex = re.compile(r'^\d{3} \d{3}-\d{4}$')
    match = phone_regex.search(input)
    return True if match else False


print(is_valid_phone("132 789-4562"))
print(is_valid_phone("132 789-4562 dfg"))
print(is_valid_phone("dd 132 789-4562 dg"))


# check if entire string is a phone number using fullmatch
def is_valid_phone2(input):
    phone_regex = re.compile(r'\d{3} \d{3}-\d{4}')
    match = phone_regex.fullmatch(input)
    return True if match else False


print(is_valid_phone2("132 789-4562"))
print(is_valid_phone2("132 789-4562 dfg"))
print(is_valid_phone2("dd 132 789-4562 dg"))

print("----------------------------")


# time validate
def is_valid_time(str_time):
    time_regex = re.compile(r'^[1-9]?[0-9]{1}:[0-9]{2}$')
    match = time_regex.search(str_time)
    return True if match else False


print(is_valid_time("10:45"))
print(is_valid_time("1:23"))
print(is_valid_time("1.23"))
print(is_valid_time("1223"))


print("----------------------------")
# groups in regex
url_regex = re.compile(r'(https?)://(www\.[A-Za-z-]{2,256}\.[a-z]{2,6})([-a-zA_Z0-9@:%_\+.~#?&//=]*)')
match = url_regex.search("http://www.youtube.com/videos/dfg/hgytg/ggd")
print(match.group(0))
print(f"Protocol: {match.group(1)}")
print(f"Domain: {match.group(2)}")
print(f"Everything else: {match.group(3)}")

print(match.groups())

print("----------------------------")


# return a list of the binary bytes contained in the string
def parse_bytes(input_str):
    byte_regex = re.compile(r"\b[01]{8}\b")
    return byte_regex.findall(input_str)


print(parse_bytes("11010101 101 323"))
print(parse_bytes("my data is: 10101010 11100010"))
print(parse_bytes("sdfdsf"))

print("----------------------------")


# named groups in regex
def parse_name(input):
    name_regex = re.compile(r'^(Mr\.|Mrs\.|Ms\.|Mdme\.) (?P<first>[A-Za-z]+) (?P<last>[A-Za-z]+)$')
    matches = name_regex.search(input)
    print(matches.group())
    print(matches.group('first'))
    print(matches.group('last'))


parse_name("Mrs. Tilda Swinton")

print("----------------------------")


def parse_date(str_date):
    date_regex = re.compile(r"^(?P<d>\d{2})[.,/](?P<m>\d{2})[.,/](?P<y>\d{4})$")
    matches = date_regex.search(str_date)
    if matches:
        return {
            'd': matches.group('d'),
            'm': matches.group('m'),
            'y': matches.group('y')
        }
    return None


print(parse_date("01/22/1999"))
print(parse_date("12,04,2003"))
print(parse_date("12.11.2003"))
print(parse_date("12.11.200312"))


print("----------------------------")
# compilation flags in regex
email_regex = re.compile(r'^([a-z0-9_\.-]+)@([0-9a-z\.-]+)\.([a-z\.]{2,6})$')
email_regex2 = re.compile(r"""
    ^([a-z0-9_\.-]+)    # first part of e-mail
    @                   # single @ sign
    ([0-9a-z\.-]+)      # e-mail provider
    \.                  # single period
    ([a-z\.]{2,6})$     # com, org, net, etc.
""", re.VERBOSE | re.IGNORECASE)

match = email_regex2.search("Thomas132@gMail.com")
print(match.group())
print(match.groups())


print("----------------------------")
# sub method in regex (replace)
text = "Last night Mrs. Daisy and Mr. White murdered Ms. Chow"
pattern = re.compile(r'(Mr\.|Mrs\.|Ms\.) ([a-z])[a-z]+', re.IGNORECASE)
# result = pattern.sub("REDACTED", text)
# result = pattern.sub("\g<1> REDACTED", text)
result = pattern.sub("\g<1> \g<2>", text)
print(result)

print("----------------------------")


def censor(text):
    pattern = re.compile(r'\bfrack[a-z]*\b', re.IGNORECASE)
    return pattern.sub("CENSORED", text)


print(censor("Frack you"))
print(censor("I hope you fracking die"))
print(censor("you fracking Frack"))
