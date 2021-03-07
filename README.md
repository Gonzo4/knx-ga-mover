# knx-ga-mover

Move blocks of KNX group addresses in a middle group by XML export/import.

1. XML Export in ETS by selecting middle group => GA export.
1. Open the xml and add new sub-address by adding =newAddress behind the old sub address (see images below). All following addresses are moved accordingly.
1. Run the script and select the xml.
1. Delete old GAs in ETS.
1. Import the xml by selecting the empty middle group => GA import.

Testet with Python 3.9.1

![Image 1](/images/1.png)
![Image 2](/images/2.png)
![Image 3](/images/3.png)