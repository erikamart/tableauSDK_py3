from tableausdk import Extract as tde # **Module change from py2 for py3
from tableausdk import Types as tdeTypes # **
import os

#Step 1: Create the Extract File
if os.path.isfile('trivialExample.tde'):
    os.remove('trivialExample.tde')

tdefile = tde.Extract('trivialExample.tde')

#Step 2: Create the tableDef
tableDef = tde.TableDefinition()
tableDef.addColumn('rowID', tdeTypes.Type.CHAR_STRING) # Column index 0. **
tableDef.addColumn('value', tdeTypes.Type.DOUBLE) #Column index 1. **

#Step 3: Create the table in the image of the tableDef
table = tdefile.addTable('Extract', tableDef)

#Step 4: Create some rows and insert them into the table
newrow = tde.Row(tableDef)
for i in range(1, 101):
    newrow.setCharString(0, 'Row '+ str(i))
    newrow.setDouble(1,i)
    table.insert(newrow)

#Step 5: Close the tde
tdefile.close()
