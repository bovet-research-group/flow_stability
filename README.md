# Repository Coverage

[Full report](https://htmlpreview.github.io/?https://github.com/bovet-research-group/flow_stability/blob/python-coverage-comment-action-data/htmlcov/index.html)

| Name                                               |    Stmts |     Miss |   Cover |   Missing |
|--------------------------------------------------- | -------: | -------: | ------: | --------: |
| src/flowstab/\_cython\_sparse\_stoch\_subst.py     |       23 |        1 |     96% |        40 |
| src/flowstab/flow\_stability.py                    |      231 |       79 |     66% |142, 159-160, 167-170, 264, 356, 375, 493-498, 517-542, 554, 572-582, 594, 612-622, 639-682, 700-721 |
| src/flowstab/helpers.py                            |       10 |        0 |    100% |           |
| src/flowstab/logger.py                             |       21 |        0 |    100% |           |
| src/flowstab/network\_clustering.py                |      969 |      873 |     10% |55-56, 97-124, 135, 150-157, 169-173, 189-192, 208-232, 243-244, 248, 262-275, 338-425, 449-457, 472-498, 519-521, 540, 574-607, 638-676, 682, 700-702, 712-812, 826-865, 871-885, 904-992, 996-1007, 1011, 1016, 1020, 1024, 1028-1029, 1033-1036, 1041-1043, 1048, 1103-1114, 1125-1128, 1139-1156, 1168-1185, 1199-1218, 1229-1331, 1339-1345, 1353, 1359, 1372-1405, 1408-1416, 1420, 1425, 1429, 1433, 1437, 1441, 1446, 1463-1477, 1536-1620, 1631, 1644-1647, 1658-1675, 1687-1698, 1712-1723, 1735-1747, 1751, 1809-1935, 1941-1958, 1971-2067, 2121-2149, 2158-2183, 2200-2256, 2270-2341, 2353-2373, 2415-2492, 2499, 2528-2549, 2556-2589 |
| src/flowstab/parallel\_clustering.py               |       93 |       76 |     18% |45-101, 106, 114-118, 124-140, 146-170, 174-198, 204-229, 233-246 |
| src/flowstab/parallel\_expm.py                     |      109 |       94 |     14% |39-43, 47-60, 92-122, 127-143, 147, 179-268 |
| src/flowstab/scripts/run\_clusterings.py           |      462 |      462 |      0% |    42-994 |
| src/flowstab/scripts/run\_cov\_integrals.py        |      339 |      339 |      0% |    41-740 |
| src/flowstab/scripts/run\_laplacians\_transmats.py |      253 |      253 |      0% |    31-571 |
| src/flowstab/sparse\_stoch\_mat.py                 |      437 |      214 |     51% |48-49, 57-58, 180, 191, 227-233, 240-249, 261, 269, 275, 286, 295, 303-307, 313, 317-322, 327, 335-363, 370, 375-402, 406-409, 417-505, 512-515, 520-529, 535, 560-589, 648, 665, 702, 718, 763, 783-786, 910, 921-935, 939-949, 966-978, 995-1008, 1030-1071, 1080-1093, 1104-1117, 1138-1151, 1184-1212, 1221-1224, 1234-1239 |
| src/flowstab/state\_tracking.py                    |      154 |        3 |     98% |73, 78, 84 |
| src/flowstab/synth\_temp\_network.py               |      276 |      117 |     58% |133, 153, 159, 164, 183, 188, 203, 208, 278, 285-287, 299, 327, 331, 337, 341-345, 378, 402, 426, 433-509, 584-586, 597, 638-640, 647-731 |
| src/flowstab/temporal\_network.py                  |     1023 |      818 |     20% |136, 146-151, 161-174, 180, 193, 271-314, 358-404, 457-566, 579-692, 703-788, 802-872, 886-959, 969-1043, 1127-1139, 1199, 1206-1208, 1213-1215, 1223-1254, 1322-1326, 1383-1446, 1472-1564, 1578-1657, 1669-1738, 1746-1777, 1812-1822, 1853-1902, 1953-1974, 1992-2100, 2123, 2155, 2198-2218, 2236-2272, 2299-2359, 2368-2375, 2379-2401, 2416-2421, 2437-2490, 2528-2565, 2598-2614, 2631-2635, 2643, 2651-2668 |
| **TOTAL**                                          | **4400** | **3329** | **24%** |           |


## Setup coverage badge

Below are examples of the badges you can use in your main branch `README` file.

### Direct image

[![Coverage badge](https://raw.githubusercontent.com/bovet-research-group/flow_stability/python-coverage-comment-action-data/badge.svg)](https://htmlpreview.github.io/?https://github.com/bovet-research-group/flow_stability/blob/python-coverage-comment-action-data/htmlcov/index.html)

This is the one to use if your repository is private or if you don't want to customize anything.

### [Shields.io](https://shields.io) Json Endpoint

[![Coverage badge](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/bovet-research-group/flow_stability/python-coverage-comment-action-data/endpoint.json)](https://htmlpreview.github.io/?https://github.com/bovet-research-group/flow_stability/blob/python-coverage-comment-action-data/htmlcov/index.html)

Using this one will allow you to [customize](https://shields.io/endpoint) the look of your badge.
It won't work with private repositories. It won't be refreshed more than once per five minutes.

### [Shields.io](https://shields.io) Dynamic Badge

[![Coverage badge](https://img.shields.io/badge/dynamic/json?color=brightgreen&label=coverage&query=%24.message&url=https%3A%2F%2Fraw.githubusercontent.com%2Fbovet-research-group%2Fflow_stability%2Fpython-coverage-comment-action-data%2Fendpoint.json)](https://htmlpreview.github.io/?https://github.com/bovet-research-group/flow_stability/blob/python-coverage-comment-action-data/htmlcov/index.html)

This one will always be the same color. It won't work for private repos. I'm not even sure why we included it.

## What is that?

This branch is part of the
[python-coverage-comment-action](https://github.com/marketplace/actions/python-coverage-comment)
GitHub Action. All the files in this branch are automatically generated and may be
overwritten at any moment.