"""
Write a script that, given a web server log file, returns the 10 most frequently
requested objects and their cumulative bytes transferred. Only include GET
requests with Successful (HTTP 2xx) responses. Resolve ties however you’d like.

Log format:
- request date, time, and time zone
- request line from the client
- HTTP status code returned to the client
- size (in bytes) of the returned object

Given this input data:
```
[01/Aug/1995:00:54:59 -0400] "GET /images/opf-logo.gif HTTP/1.0" 200 32511
[01/Aug/1995:00:55:04 -0400] "GET /images/ksclogosmall.gif HTTP/1.0" 200 3635
[01/Aug/1995:00:55:06 -0400] "GET /images/ksclogosmall.gif HTTP/1.0" 403 298
[01/Aug/1995:00:55:09 -0400] "GET /images/ksclogosmall.gif HTTP/1.0" 200 3635
[01/Aug/1995:00:55:18 -0400] "GET /images/opf-logo.gif HTTP/1.0" 200 32511
[01/Aug/1995:00:56:52 -0400] "GET /images/ksclogosmall.gif HTTP/1.0" 200 3635
```

The result should be:
```
/images/ksclogosmall.gif 10905
/images/opf-logo.gif 65022
```

(You may tweak the output format as you'd like)
"""

def get_most_requested(log_file):
    """ Prints the file path and cumulative bytes transferred to the command
        line in descending order of times requested.

    """

    if not log_file:
        return None

    with open(log_file) as log:
        requests = [line.strip() for line in log.readlines()]

    files = {}

    for request in requests:
        _, _, r_type, r_file, _, r_status, t_bytes = request.split()
        # Ignore non-GET and unsuccessful requests
        if r_type != '"GET' or r_status[0] != '2':
            continue
        # Log each unique file; increment request count and add bytes
        files[r_file] = files.get(r_file, [0, 0])
        files[r_file][0] += 1  # Increment request count
        files[r_file][1] += int(t_bytes)  # Increase total t_bytes

    # Print first 10 files' name and total t_bytes desc-sorted by request count
    for item in sorted(files.items(), key=lambda f: f[1][0], reverse=True)[:10]:
        print(item[0], item[1][1])
