#!/bin/env python

class PeriodicLogger():
	""" outputs message only periodically (not queued) """
	_DEFAULT_PERIOD = 100

	def __init__(self, period=_DEFAULT_PERIOD):
		self.reset(period)
	
	def _should_log(self):
		i = 0
		while True:
			if i % self._period == 0:
				yield True
			i += 1
			yield False
	
	def reset(self, period=_DEFAULT_PERIOD):
		self._is_time = self._should_log()
		self._period = period

	def log(self, msg):
		try:
			if next(self._is_time):
				print(msg)
		except:
			pass
