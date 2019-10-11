# ACID and Database Scalability Tradeoffs

Comparing the costs and benefits of relational and non-relational approaches -
can we have the best of both worlds?

## Learning Objectives

- Understand and explain the advantages and disadvantages of traditional SQL
  databases
- Make informed decisions about alternative databases

## Before Lecture

So far in this sprint you've used SQLite, PostgreSQL, and MongoDB. For each of
these, consider the following questions:

- What was easy about using this technology?
- What was hard about using this technology?
- What more would you like to learn about it?

Write a summary in the style of a possible blog post, and bring the
questions/discussion to class. Bonus - later on, follow up and complete a real
blog post about different database technologies!

## Live Lecture Task

We covered a lot of ground this week - today we'll bring it together, both
summarizing and resolving lingering questions. We'll also continue the
discussion from the before lecture activity, and explore the cutting edge
"NewSQL" techniques in active development.

As time allows, we'll go back to practicing good old SQL. It's important to have
a broad awareness of the database universe, but SQL is a time-tested tool that
has and will continue to be useful across a wide range of situations. It will
also be the largest part of the sprint challenge, and likely a component of many
job interviews.

## Assignment

Practice! Go back to both your deployed PostgreSQL (Titanic data) and MongoDB
(RPG data) instances - use [MongoDB
queries](https://docs.mongodb.com/manual/tutorial/query-documents/) to answer
the same questions as you did from the first module (when the RPG data was in
SQLite). With PostgreSQL, answer the following:

- How many passengers survived, and how many died?
  - 887 survived
  - 545 died
- How many passengers were in each class?
  - (1, 216), (3, 487), (2, 184)
- How many passengers survived/died within each class?
  - Survived by class: (1, 136), (3, 119), (2, 87)
  - Died by class:     (1, 80),  (3, 368), (2, 97)
- What was the average age of survivors vs nonsurvivors?
  - Avg. survivor age:     28.41
  - Avg. non-survivor age: 30.15
- What was the average age of each passenger class?
  1. 38.79
  2. 29.88
  3. 25.20
- What was the average fare by passenger class? By survival?
  - Avg. fare by class:
    1. $84.15
    2. 20.66
    3. 13.70
  - Avg. fare by survival:
    - Non-survivors: $30.15
    - Survivors: $28.41
- How many siblings/spouses aboard on average, by passenger class? By survival?
  - By Class:
    1. 0.416
    2. 0.402
    3. 0.62
  - By Survival:
    - Non-survivors: 0.5577
    - Survivors: 0.4736
- How many parents/children aboard on average, by passenger class? By survival?
  - By Class:
    1. 0.356
    2. 0.380
    3. 0.396
  - By Survival:
    - Non-survivors: 0.3321
    - Survivors: 0.4649
- Do any passengers have the same name?
  - "select first, count(first) from (select split_part(Name, ' ', 3) as first from titanic) as names group by first order by count(first) desc"
  - # passengers by first name: ('William', 48), ('John', 31), ('Thomas', 18), ('George', 16), ('Charles', 16), ('James', 15), ('Henry', 15), ('Frederick', 13), ('Edward', 13), ('Richard', 11), ('Johan', 10), ('Mary', 9), ('Anna', 9), ('Samuel', 9), ('Karl', 9), ('Joseph', 9), ('Arthur', 7), ('Alfred', 7), ('Albert', 7), ('Margaret', 6), ('Victor', 6), ('Peter', 6), ('Elizabeth', 6), ('Ernest', 6), ('Robert', 6), ('Frank', 5), ('Alexander', 5), ('Ernst', 5), ('Alice', 5), ('Walter', 5), ('Harry', 5), ('Daniel', 4), ('Ivan', 4), ('Nils', 4), ('Hans', 4), ('Benjamin', 4), ('Sidney', 4), ('Percival', 4), ('Ellen', 4), ('Helen', 4), ('Martin', 4), ('Bertha', 4), ('August', 4), ('David', 4), ('Patrick', 4), ('Leo', 3), ('Francis', 3), ('Juha', 3), ('Katherine', 3), ('Emil', 3), ('Anders', 3), ('Kate', 3), ('Jean', 3), ('Annie', 3), ('Jakob', 3), ('Stephen', 3), ('Rene', 3), ('Hanna', 3), ('Reginald', 3), ('Carl', 3), ('Hanora', 3), ('Tannous', 3), ('Augusta', 3), ('Mauritz', 2), ('Madeleine', 2), ('Michel', 2), ('Juho', 2), ('Emily', 2), ('(Elizabeth', 2), ('Lewis', 2), ('Ida', 2), ('Pekka', 2), ('Edvard', 2), ('Bertram', 2), ('Frederic', 2), ('Hugh', 2), ('Lawrence', 2), ('Norman', 2), ('Marion', 2), ('Wilhelm', 2), ('Jacques', 2), ('Manuel', 2), ('Sinai', 2), ('Matti', 2), ('Anthony', 2), ('Amin', 2), ('Josef', 2), ('Leonard', 2), ('Andrew', 2), ('Mabel', 2), ('Marie', 2), ('Viktor', 2), ('Dickinson', 2), ('Harold', 2), ('Johannes', 2), ('Edgar', 2), ('Lalio', 2), ('Elsie', 2), ('Lillian', 2), ('Hudson', 2), ('Eino', 2), ('Harvey', 2), ('Timothy', 2), ('Antti', 2), ('Washington', 2), ('Luka', 2), ('Nicholas', 2), ('Bridget', 2), ('Marija', 2), ('Lee', 2), ('Eugene', 2), ('Marjorie', 2), ('Edwy', 2), ('Amelia', 2), ('Owen', 2), ('Jacob', 2), ('Stanley', 2), ('Gustaf', 2), ('Constance', 2), ('Antoni', 2), ('Catherine', 2), ('Maurice', 2), ('Elmer', 2), ('Gerious', 2), ('Susan', 2), ('Erik', 2)
  - # passengers by last name: ('Andersson', 9), ('Sage', 7), ('Skoog', 6), ('Goodwin', 6), ('Carter', 6), ('Johnson', 6), ('Panula', 6), ('Rice', 5), ('Harper', 4), ('Hart', 4), ('Williams', 4), ('Asplund', 4), ('Palsson', 4), ('Lefebre', 4), ('Baclini', 4), ('Harris', 4), ('Kelly', 4), ('Fortune', 4), ('Brown', 4), ('Gustafsson', 4), ('Ford', 4), ('Navratil', 3), ('Hickman', 3), ('Laroche', 3), ('Olsen', 3), ('Newell', 3), ('Taussig', 3), ('Meyer', 3), ('Planke', 3), ('Moran', 3), ('Smith', 3), ('Richards', 3), ('Bourke', 3), ('OBrien', 3), ('Boulos', 3), ('Hansen', 3), ('Goldsmith', 3), ('Graham', 3), ('Collyer', 3), ('Davies', 3), ('Flynn', 3), ('Hoyt', 3), ('Jussila', 3), ('Allison', 3), ('Jensen', 3), ('Elias', 3), ('Thayer', 3), ('Johansson', 3), ('Impe', 3), ('West', 3), ('Peter', 2), ('Lobb', 2), ('Hays', 2), ('Minahan', 2), ('Carlsson', 2), ('Rosblom', 2), ('Jacobsohn', 2), ('Thorneycroft', 2), ('Andrews', 2), ('Attalah', 2), ('Zabour', 2), ('Mellinger', 2), ('Hakkarainen', 2), ('Keane', 2), ('Svensson', 2), ('Crosby', 2), ('Futrelle', 2), ('Barbara', 2), ('Kantor', 2), ('Renouf', 2), ('Petroff', 2), ('Hamalainen', 2), ('Baxter', 2), ('Moubarek', 2), ('Becker', 2), ('Braund', 2), ('Mallet', 2), ('Allen', 2), ('Quick', 2), ('Morley', 2), ('Nicola-Yarred', 2), ('Nakid', 2), ('White', 2), ('Ryerson', 2), ('Arnold-Franchi', 2), ('Johnston', 2), ('Olsson', 2), ('Sandstrom', 2), ('Stanley', 2), ('Castellana', 2), ('Hagland', 2), ('Danbom', 2), ('Goldenberg', 2), ('Holverson', 2), ('Yasbeck', 2), ('Chambers', 2), ('Beane', 2), ('Gordon', 2), ('Dean', 2), ('Larsson', 2), ('Daly', 2), ('Saad', 2), ('Moor', 2), ('McCoy', 2), ('Cacic', 2), ('Abbott', 2), ('Turpin', 2), ('Calic', 2), ('Coutts', 2), ('Oreskovic', 2), ('Wick', 2), ('Herman', 2), ('Doling', 2), ('Chapman', 2), ('Hippach', 2), ('Silvey', 2), ('Pears', 2), ('Strom', 2), ('Bishop', 2), ('Caldwell', 2), ('Webber', 2), ('Hocking', 2), ('Ali', 2), ('Murphy', 2), ('Lam', 2), ('Coleff', 2), ('Nasser', 2), ('Taylor', 2), ('Backstrom', 2), ('Beckwith', 2), ('Abelson', 2), ('Frauenthal', 2), ('Dick', 2)
- (Bonus! Hard, may require pulling and processing with Python) How many married
  couples were aboard the Titanic? Assume that two people (one `Mr.` and one
  `Mrs.`) with the same last name and with at least 1 sibling/spouse aboard are
  a married couple.

## Resources and Stretch Goals

The assignment drilled core SQL, but *didn't* review joins - revisit the RPG
data, and do more joins (explicit or implicit) to make sure you understand how
to connect data across tables.

If you got the Titanic data in your MongoDB cluster - see if you can also answer
the above questions using MongoDB!

Read up on [database
normalization](https://en.wikipedia.org/wiki/Database_normalization) - a variety
of formal techniques for reducing the redundancy of data stored in a relational
database.

Keep working on your written summary from the "before lecture" exercise, and
grow it into a proper blog post. Consider focusing it on one particular
technology or technique, and compare/contrast it with the alternatives.

Get more reps in! Check out [SQLBolt](https://sqlbolt.com/) and [w3schools SQL
Tutorial](https://www.w3schools.com/sql/), both of which include interactive
exercises. Mastering SQL is all about practice, so get it down now and you'll be
confident for your job interviews.
