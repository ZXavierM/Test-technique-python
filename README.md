# Python Developer Assessment

The purpose of this Python assessment is to determine the experience level of the candidate, it is not a binary pass/fail test. It is to assess on which level the developer is. It should be seen as a validation process and there are no right or wrong ways to solve the defined tasks.

There are seven tasks to be completed, based on a list of cadastres representing wine parcels with their characteristics. Each task aims to test a developer's ability to manipulate and modify a list of data.

> The data can be found in the `/cadastres/resouces/data.py` file.

The data can be viewed by running the following commands on the command line in Python's interactive mode (**_Don't forget to install Python on your system first_**):

```bash
python
>>> from cadastres.resources.data import CADASTRES
>>> print(CADASTRES)
```

You can then exit terminal using:

```bash
exit()
```

The data structure is represented as follows:

```python
[
    {
        "type": "Feature",
        "properties": {
            "type_prod": "Vins",
            "categorie": "Vin tranquille",
            "type_denom": "appellation",
            "type_ig": "AOC",
            "id_app": "178",
            "appellatio": "Criots-Bâtard-Montrachet",
            "id_denom": "564",
            "denominati": "Criots-Bâtard-Montrachet",
            "new_insee": "21150",
            "new_nomcom": "CHASSAGNE-MONTRACHET",
            "old_insee": "21150",
            "old_nomcom": "CHASSAGNE-MONTRACHET",
            "id_aire": "476",
            "crinao": "Bourgogne, Beaujolais, Savoie, Jura",
            "dt": "Dijon",
        },
        "geometry": {"type": "Polygon", "coordinates": [...]},
    },
    {
        "type": "Feature",
        "properties": {
            "type_prod": "Vins",
            "categorie": "Vin tranquille",
            "type_denom": "dénomination géographique complémentaire",
            "type_ig": "AOC",
            "id_app": "134",
            "appellatio": "Beaune",
            "id_denom": "312",
            "denominati": "Beaune premier cru Blanches Fleurs",
            "new_insee": "21054",
            "new_nomcom": "BEAUNE",
            "old_insee": "21054",
            "old_nomcom": "BEAUNE",
            "id_aire": "223",
            "crinao": "Bourgogne, Beaujolais, Savoie, Jura",
            "dt": "Dijon",
        },
        "geometry": {"type": "Polygon", "coordinates": [...]},
    },
    ...
]
```

## Assessment Instructions

To complete the assessment please clone the repository.

```
git clone https://closandmonopole@dev.azure.com/closandmonopole/Hiring%20Assessments/_git/Python
```

Write your code to accomplish the tasks and store it in a public git repository on GitHub or an equivalent service. You can also zip up your code and submit it by email. The first option will be more appreciated and will help us to understand how you use Git tool.

## Tasks

Create one file for each task you will perform.

### Task 1: Find One

Find and return the `second item` in the list.

**Output:** The below dictionary should the item returned.

```python
{
        "type": "Feature",
        "properties": {
            "type_prod": "Vins",
            "categorie": "Vin primeur, Vin tranquille",
            "type_denom": "appellation",
            "type_ig": "AOC",
            "id_app": "138",
            "appellatio": "Bourgogne",
            "id_denom": "362",
            "denominati": "Bourgogne",
            "new_insee": "71294",
            "new_nomcom": "MERCUREY",
            "old_insee": "71294",
            "old_nomcom": "MERCUREY",
            "id_aire": "1781",
            "crinao": "Bourgogne, Beaujolais, Savoie, Jura",
            "dt": "Dijon",
        }
        ...
}
```

### Task 2: Find Data

Find and return a new list of data where each item's appelation is `Bourgogne`.

**Example:** The below dictionary should be one of the items returned in the new list.

```python
{
        "type": "Feature",
        "properties": {
            "type_prod": "Vins",
            "categorie": "Vin primeur, Vin tranquille",
            "type_denom": "appellation",
            "type_ig": "AOC",
            "id_app": "138",
            "appellatio": "Bourgogne",
            "id_denom": "362",
            "denominati": "Bourgogne",
            "new_insee": "71294",
            "new_nomcom": "MERCUREY",
            "old_insee": "71294",
            "old_nomcom": "MERCUREY",
            "id_aire": "1781",
            "crinao": "Bourgogne, Beaujolais, Savoie, Jura",
            "dt": "Dijon",
        }
        ...
}
```

### Task 3: Find the "Premiers Crus"

Find and return a new list of data where item(s) is/are a `premier cru`.

**Example:** The below dictionary should be one of the items returned in the new list.

```python
{
        "type": "Feature",
        "properties": {
            "type_prod": "Vins",
            "categorie": "Vin tranquille",
            "type_denom": "dénomination géographique complémentaire",
            "type_ig": "AOC",
            "id_app": "134",
            "appellatio": "Beaune",
            "id_denom": "312",
            "denominati": "Beaune premier cru Blanches Fleurs",
            "new_insee": "21054",
            "new_nomcom": "BEAUNE",
            "old_insee": "21054",
            "old_nomcom": "BEAUNE",
            "id_aire": "223",
            "crinao": "Bourgogne, Beaujolais, Savoie, Jura",
            "dt": "Dijon",
        }
        ...
}
```

### Task 4: Amend Data

Add property `classification` to each element that is a `premier cru`, add to them the value `PR` and `N/A` for the others.

**Example:** An amended dictionary should look as below where the dictionary has now the `classification` property.

```python
{
        "type": "Feature",
        "properties": {
            "type_prod": "Vins",
            "categorie": "Vin tranquille",
            "type_denom": "dénomination géographique complémentaire",
            "type_ig": "AOC",
            "id_app": "134",
            "appellatio": "Beaune",
            "id_denom": "312",
            "denominati": "Beaune premier cru Blanches Fleurs",
            "new_insee": "21054",
            "new_nomcom": "BEAUNE",
            "old_insee": "21054",
            "old_nomcom": "BEAUNE",
            "id_aire": "223",
            "crinao": "Bourgogne, Beaujolais, Savoie, Jura",
            "dt": "Dijon",
            "classification": "PR"
        }
        ...
}
```

### Task 5: Cleanse Data

Find and change each item containing the word `premier cru` to `1er cru` for clarity.

**Example:** The below dictionary should be one of the items returned in the new list.

```python
{
        "type": "Feature",
        "properties": {
            "type_prod": "Vins",
            "categorie": "Vin tranquille",
            "type_denom": "dénomination géographique complémentaire",
            "type_ig": "AOC",
            "id_app": "134",
            "appellatio": "Beaune",
            "id_denom": "312",
            "denominati": "Beaune 1er cru Blanches Fleurs",
            "new_insee": "21054",
            "new_nomcom": "BEAUNE",
            "old_insee": "21054",
            "old_nomcom": "BEAUNE",
            "id_aire": "223",
            "crinao": "Bourgogne, Beaujolais, Savoie, Jura",
            "dt": "Dijon"
        }
        ...
}
```

### Task 6: Geometry

Each item in the list has a geometric coordinate array.
These coordinates represented by a multidimensional array (`"coordinates": [[x.xxxxxx, x.xxxxxx] ... ]`) determine the latitude and longitude of each of these coordinates. For each item, return a new list with their sum of coordinates.

**Example:** For this data, we have three coordinates. Pay attention to geometry type that can be either `Polygon` or `MultiPolygon`.

```json
{
  "type": "Polygon",
  "coordinates": [
    [
      [839462.817, 6662220.16],
      [839477.0, 6662212.105],
      [839448.181, 6662160.253]
    ]
  ]
}
```

**Expected Output:**

```python
{
        "type": "Feature",
        "properties": {
            "type_prod": "Vins",
            "categorie": "Vin primeur, Vin tranquille",
            "type_denom": "appellation",
            "type_ig": "AOC",
            "id_app": "138",
            "appellatio": "Bourgogne",
            "id_denom": "362",
            "denominati": "Bourgogne",
            "new_insee": "71294",
            "new_nomcom": "MERCUREY",
            "old_insee": "71294",
            "old_nomcom": "MERCUREY",
            "id_aire": "1781",
            "crinao": "Bourgogne, Beaujolais, Savoie, Jura",
            "dt": "Dijon",
        },
        "geometry": {
            "coordinates_count": 3
        }
        ...
}
```

> You are free to keep the other contained data in the geometry or just set the `coordinates_count` property. At your convenience.

### (optional) Task 7 : Challenge !

This last task is there to assess your ability to find a technical solution without clues or examples. You must respond to a functional request after having made your own research which appears to you to be the most suitable to solve this request.

**Instruction:**

Give the center point of each cadastre, exemple `[839462.817, 6662220.16]`. Returned dictionary can be any shape you want. Because we're nice, we still give you a hint. There are many algorithms or libs available to do this, Google is your friend.
