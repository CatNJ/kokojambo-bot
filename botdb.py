import sqlite3

db = sqlite3.connect('user.db')
cur = db.cursor()

class User:
	__user_id = None
	__status = None
	__money = None
	__size_huy = None
	__lvl_ok = None

	def __init__(self, user_id):
		self.user_id = user_id


	def check_user(self, user_id):
		cur.execute(f"SELECT {self.user_id} FROM users WHERE user_id")
		if cur.fetchone() == None:
			cur.execute("INSERT INTO users VALUES( ?, ?, ?, ?, ?, ? );", (user_id, 'Игрок', 10000, 0, 1, 'Безработный'))
			db.commit()

	def user_info(self, user_id):
		cur.execute(f"SELECT * FROM users WHERE user_id = {self.user_id}")
		return cur.fetchone()



	def get_money(self, money):
		cur.execute(f'SELECT money FROM users WHERE user_id = {self.user_id}')
		user_money = cur.fetchone()[0]
		cur.execute(f"""UPDATE users SET money = {money + user_money}
			WHERE user_id = {self.user_id}
		""")
		db.commit()


	def huy_size(self, size_huy):
		cur.execute(f"""UPDATE users SET huy_size = {size_huy}
			WHERE user_id = {self.user_id}
		""")


	def lvl_top(self):
		cur.execute(f'SELECT lvl FROM users WHERE user_id = {self.user_id}')
		user_lvl = cur.fetchone()[0]

		min_lvl = 15

		lvl = 1

		num = 15

		nom = 5

		while True:
			if user_lvl < min_lvl:

				break

			else:

				lvl += 1

				min_lvl += num

				num += nom


		return lvl


	def job_add(self, jobe):
		cur.execute(f'SELECT jobs FROM users WHERE user_id = {self.user_id}')
		cur.execute(f"UPDATE users SET jobs = ? WHERE user_id = ?", (f'{jobe}', f'{self.user_id}'))

		db.commit()



