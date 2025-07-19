# MultiPad
An Multifunctional inspired macro pad. That im submiting for HackClub's <a href="highway.hackclub.com">highway</a>. The macro pad has a minimalist but functional design, With Multi layerd functionality

# Features

  - 9 Keys aranged in 3x3 Patern
  - Cherry MX Linear Switches
  - Multi Profile (3 Profiles)
  - OLED Displaying information and profile in use.

# Layout

|    OLED |        | ESP 32 |
|---------|--------|--------|
|    1    |    2   |    3   |
|    4    |    5   |    6   |
|    7    |    8   |    9   |

> [!Warning]
> The Below Features of the Firmware are NOT complete. The firmware currently only initalizes oled and functions as a numpad. this is because i find it hard to develop feautres  without having a platform to develop on.

# The Function Key

The Blue Function key is designed to allow changing of settings of the macro pad.

##  Setings

Hold down F(BLUE) key for 3 Seconds to enter customization mode. use 5 and 8 to scroll. Key 2 to modify option. Hold F Key again to exit and apply. 

Available Setings Below:


|Setting        | Options    | Desc        |
|---------------|------------|-------------|
|Toggle OLED    | On  Off    | Toggles OLED.   |
|Toggle NP      | On  Off    | Toggles NP      |
|Default Profile| 1 2 3      | Sets the Inital Profile|


## Live Switch Profile 

Hold F Key and Key 7 for 3 seconds. OLED and Neo Pixle Will light regardless of settings. and use keys 4-6 to select profile and use Key 7 to exit.

# Photos
## Case

<img width=600 src="https://github.com/Darbyshire64/MultiPad/blob/4c1d576a043a0029328d6c29cf909fc135e0a3df/FinalPics/RENDER1.png">
<img width=600 src="https://github.com/Darbyshire64/MultiPad/blob/4c1d576a043a0029328d6c29cf909fc135e0a3df/FinalPics/RENDER2.PNG">
<img width=600 src="https://github.com/Darbyshire64/MultiPad/blob/4c1d576a043a0029328d6c29cf909fc135e0a3df/FinalPics/RENDER3.PNG">
<img width=600 src="https://github.com/Darbyshire64/MultiPad/blob/4c1d576a043a0029328d6c29cf909fc135e0a3df/FinalPics/RENDER4.png">

# PCB 

<img width=500 height=400 src="https://github.com/Darbyshire64/MultiPad/blob/4c1d576a043a0029328d6c29cf909fc135e0a3df/FinalPics/3D-PCB.png">
<img width=500 height=400 src="https://github.com/Darbyshire64/MultiPad/blob/4c1d576a043a0029328d6c29cf909fc135e0a3df/FinalPics/PCB.png">
<img width=500 height=400 src="https://github.com/Darbyshire64/MultiPad/blob/4c1d576a043a0029328d6c29cf909fc135e0a3df/FinalPics/SCHEMATIC.png">



# BOM

|QTY| Item                      | *Price | Link                               |
|---|---------------------------|--------|------------------------------------|
| 9 | Cherry MX Linear          | £11.61 | <a href="https://www.digikey.co.uk/en/products/detail/cherry-americas-llc/MX2A-L1NN/21738390">Link</a>|
| 1 | Seed Studio XIAO RP2040   | £3.44  |<a href="https://www.digikey.co.uk/en/products/detail/seeed-technology-co-ltd/102010428/14672129">Link</a>|
| 1 | 0.91 OLED SSD1306 Dsiplay | N/A    | N/A |
| 5 | *Custom PCB               | $2.37  | N/A |
| 2 | *3D Printed Case          | *£0    | N/A |
| 9 | THT 1N4148 Diodes         | £0.63  |<a href="https://www.digikey.co.uk/en/products/detail/onsemi/1N4148/458603">Link</a>|
| 8 | *White DSA Keycaps        | £34.96 |<a href="https://www.digikey.co.uk/en/products/detail/adafruit-industries-llc/4998/14552195">Link</a>|
| 3 | M3 Heatset Inserts        | N/A    | N/A |
| 3 | M3x16mm Screws            | N/A    | N/A |

* Price Sourced from DigiKey UK in GBP Excluding VAT
* PCB Price from JLC PCB in usd excluding shiping or any coupons from HC.
* 2 Cases because i made two case designs.
* 8 key caps because i have 1 blue one already i would like to use
* Price is free because printed via printing legion. IDK delivery cost so 0 for now but acount for delivery

