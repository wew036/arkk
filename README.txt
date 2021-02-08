This is a very rudimentary analysis of ARKK holdings.

No license. This code is in public domain.

You need to install necessary python3 packages (PyPDF2 and yfinance) before this program can run.

ARKK holdings can be found in the ARK official website. The history of ARKK holdings were downloaded from web.archive.org.

The program hardcoded the start and end date to be 4/14/2020 to 8/6/2020.

When the program is invoked without argument, it downloads the start and end price of the above dates, and calculate the expected price change of ARKK.

The following session shows that ARKK grows by 68%. And all holdings of its stock also grow by 68% in the same period. This shows two things of ARKK (at least for the tested period):

1. The published holdings of ARKK is correct
2. ARKK did not use any leverage

Sample output of the program:

$ ./arkk.py
[*********************100%***********************]  1 of 1 completed
[*********************100%***********************]  1 of 1 completed
ARKK (2020-04-14 49.58665084838867) (2020-8-6 83.53353118896484)
EndValue / StartValue = 1.68
...

XONE (2020-04-14 6.849999904632568) (2020-8-6 9.850000381469727)
[*********************100%***********************]  1 of 1 completed
[*********************100%***********************]  1 of 1 completed
ONVO (2020-04-14 6.400000095367432) (2020-8-6 14.0)
EndValue / StartValue = 1.68
