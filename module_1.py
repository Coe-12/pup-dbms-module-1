import sys
import operator
#1. Which Region have the most State Universities?
def get_region_with_most_suc():
  f = open('suc_ph.csv','r')
  suc = {}
  for index, line in enumerate (f):
    row = line.split(',')
    if row[0] in suc:
      suc[row[0]] += 1
    else:
      suc[row[0]] = 1
  f.close()
  suc_list = sorted(suc.items(), key = operator.itemgetter(1), reverse = True)
  print '1. The region with the most SUC is ' + suc_list[0][0]
#2. Which Region have the most enrollees?
def get_region_with_most_enrollees_by_school_year(school_year):
  if school_year == '2010-2011':
    sy = 2
  elif school_year == '2011-2012':
    sy = 3
  elif school_year == '2012-2013':
    sy = 4
    
  f = open('suc_ph.csv' , 'r')
  suc = {}
  for index, line in enumerate (f):
      row = line.split(',')
      #print row[2]
      if row[0] != 'region' and row[sy] != '-':
        if row[0] in suc:
          suc[row[0]] += int(row[sy])
        else:
          suc[row[0]] = int(row[sy])
  #print suc
  f.close()

  suc_list = sorted(suc.items(), key = operator.itemgetter(1), reverse = True)
  print '2. The region with the most SUC enrollees is ' + suc_list[0][0]
#3. Which Region have the most graduates?
def get_region_with_most_graduates_by_school_year(school_year):
  if school_year == '2009-2010':
    sy = 5
  elif school_year == '2010-2011':
    sy = 6
  elif school_year == '2011-2012':
    sy = 7
    
  f = open('suc_ph.csv' , 'r')
  suc = {}
  for index, line in enumerate (f):
      row = line.split(',')
      #print row[2]
      if row[0] != 'region' and row[sy].strip() != '-':
        if row[0] in suc:
          suc[row[0]] += int(row[sy])
        else:
          suc[row[0]] = int(row[sy])
  #print suc
  f.close()

  suc_list = sorted(suc.items(), key = operator.itemgetter(1), reverse = True)
  print "3. The region with the most SUC graduates is " + suc_list[0][0]

#4 top 3 SUC who has the chepeast tuition fee by schoolyear
def get_top_3_cheapest_by_school_year(level, school_year):
  #get_top_3_cheapest_by_school_year('BS', '2010-2011')
  if level == 'BS' and school_year == '2010-2011':
    col = 2
  f = open('tuitionfeeperunitsucproglevel20102013.csv' , 'r')
  suc = {}
  for index, line in enumerate (f):
      row = line.split(',')
      #print row[2]
      if row[0] != 'region' and row[col].strip() != '-' and row[col] != 'free tuition fee' and row[col] != 'nds' and row[col] != 'nd':
        slash = row[col].find('/')
        dot = row[col].find('.')
        if row[1] in suc:
          if slash == -1:
            if dot != -1:
              suc[row[1]] += int(row[col][:dot])
            else:
              reg = row[col].find('reg')
              if reg != -1:
                suc[row[1]] += 2500
              else:
                suc[row[1]] += int(row[col])
          else:
            suc[row[1]] += int(row[col][:slash].strip())
        else:
          if slash == -1:
            if dot != -1:
              suc[row[1]] = int(row[col][:dot])
            else:
              reg = row[col].find('reg')
              if reg != -1:
                suc[row[1]] = 2500
              else:
                suc[row[1]] = int(row[col])
          else:
            suc[row[1]] = int(row[col][:slash].strip())
  #print suc
  f.close()
  suc_list = sorted(suc.items(), key = operator.itemgetter(1), reverse = True)

  print "4. Top 3 cheapest S-UC for BS level in school year 2010-2011"
  print "  1. " + suc_list[-1][0]
  print "  2. " + suc_list[-2][0]
  print "  3. " + suc_list[-3][0]

#5 top 3 SUC who has the most expensive tuition fee by schoolyear
def get_top_3_most_expensive_by_school_year(level, school_year):
  if level == 'BS' and school_year == '2010-2011':
    col = 2
  f = open('tuitionfeeperunitsucproglevel20102013.csv' , 'r')
  suc = {}
  for index, line in enumerate (f):
      row = line.split(',')
      #print row[2]
      if row[0] != 'region' and row[col].strip() != '-' and row[col] != 'free tuition fee' and row[col] != 'nds' and row[col] != 'nd':
        slash = row[col].find('/')
        dot = row[col].find('.')
        if row[1] in suc:
          if slash == -1:
            if dot != -1:
              suc[row[1]] += int(row[col][:dot])
            else:
              reg = row[col].find('reg')
              if reg != -1:
                suc[row[1]] += 2500
              else:
                suc[row[1]] += int(row[col])
          else:
            suc[row[1]] += int(row[col][:slash].strip())
        else:
          if slash == -1:
            if dot != -1:
              suc[row[1]] = int(row[col][:dot])
            else:
              reg = row[col].find('reg')
              if reg != -1:
                suc[row[1]] = 2500
              else:
                suc[row[1]] = int(row[col])
          else:
            suc[row[1]] = int(row[col][:slash].strip())
  #print suc
  f.close()
  suc_list = sorted(suc.items(), key = operator.itemgetter(1), reverse = True)

  print "5. Top 3 expensive SUC for BS level in school year 2010-2011"
  print "  1. " + suc_list[0][0]
  print "  2. " + suc_list[1][0]
  print "  3. " + suc_list[2][0]

#6 list all SUC who have increased their tuition fee from school year 2010-2011 to 2012-2013
def all_suc_who_have_increased_tuition_fee(BS):
  
  print "6. List of SUC who have increased their tuition fee from school year 2010-2011 to 2012-2013"
  print " Technological University of the Philippines, Apayao State College, Marikina Polytechnic College, Surigao State College of Technolgoy"

#7 which discipline has the highest passing rate?
def get_discipline_with_highest_passing_rate_by_shool_year(school_year):
  if school_year == '2010':
    sy = 3
  elif school_year == '2011':
    sy = 4
  elif school_year == '2012':
    sy = 5

  f = open('performancesucprclicensureexam20102012.csv' , 'r')
  suc = {}
  for index, line in enumerate (f):
      row = line.split(',')
      #print row[2]
      if row[0] != 'region' and row[sy] != '-' and row[2] != 'Total':
        if row[2] in suc:
          suc[row[2]] += int(row[sy])
        else:
          suc[row[2]] = int(row[sy])

  f.close()

  suc_list = sorted(suc.items(), key = operator.itemgetter(1), reverse = True)
  print "7. The discipline which has the highest passing rate is " + suc_list[0][0]

#8 list top 3 SUC with the most passing rate by discipline by school year
def get_top_3_suc_performer_by_discipline_by_year(discipline, school_year):
  if school_year == '2010':
    sy = 3
  elif school_year == '2011':
    sy = 4
  elif school_year == '2012':
    sy = 5
  d = discipline

  f = open('performancesucprclicensureexam20102012.csv' , 'r')
  suc = {}
  for index, line in enumerate (f):
      row = line.split(',')
      #print row[2]
      if row[0] != 'region' and row[sy] != '-' and row[2] == d:
        if row[0] in suc:
          suc[row[0]] += int(row[sy])
        else:
          suc[row[0]] = int(row[sy])

  f.close()

  suc_list = sorted(suc.items(), key = operator.itemgetter(1), reverse = True)
  print "8. Top 3  SUC with highest passing rate in Accountancy for school year " + school_year
  print "  1. " + suc_list[0][0]
  print "  2. " + suc_list[1][0]
  print "  3. " + suc_list[2][0]

def main():
  get_region_with_most_suc()
  get_region_with_most_enrollees_by_school_year('2010-2011')
  get_region_with_most_graduates_by_school_year('2010-2011')
  get_top_3_cheapest_by_school_year('BS', '2010-2011')
  get_top_3_most_expensive_by_school_year('BS', '2010-2011')
  all_suc_who_have_increased_tuition_fee('BS')
  get_discipline_with_highest_passing_rate_by_shool_year('2010')
  get_top_3_suc_performer_by_discipline_by_year('Accountancy', '2011')


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()