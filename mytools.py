from pyreadstat import pyreadstat


国家认同调查数据表, metadata = pyreadstat.read_sav(R'data\identity.sav',apply_value_formats=True,formats_as_ordered_category=True)
国家认同调查数据表, metadata = pyreadstat.read_sav(R'data\identity.sav',apply_value_formats=True,formats_as_ordered_category=True)
result = 国家认同调查数据表['会打多少分'].value_counts(sort=False)