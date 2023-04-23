import apache_beam as beam

from log_elements import LogElements

with beam.Pipeline() as pi:

  (pi | beam.Create(range(1, 20))
     | beam.combiners.Top.Largest(2)
     | LogElements())

