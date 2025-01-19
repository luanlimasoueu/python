
import sqlite3 as lit
 
def main():
   try:
       db = lit.connect('geekscoders.db')
       print("Database created", db)
       db.cursor()
 
   except:
       print("failed to create database")
 
 
 
if __name__ == "__main__":
      main()