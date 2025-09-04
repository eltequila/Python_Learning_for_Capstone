import datetime

class PreySample:
    def __init__(self, full_species_name, delta13c_list, tissue_description, sample_date_utc):
        self.full_species_name = full_species_name
        self.delta13c_list = delta13c_list
        self.tissue_description = tissue_description
        self.sample_date_utc = sample_date_utc

    def get_common_name(self):
        parts_name = self.full_species_name.split('(')
        common_name = parts_name[0].strip()
        return common_name

    def get_scientific_name(self):
        parts_name = self.full_species_name.split('(')
        scientific_name = parts_name[1].replace(')', '')
        return scientific_name

    def average_delta13c(self):
        sum_delta13c = sum(self.delta13c_list)
        len_delta13c = len(self.delta13c_list)
        return sum_delta13c / len_delta13c

    def get_tissue_count(self):
        tissue_words = self.tissue_description.split(',')
        tissue_count = len(tissue_words)
        return tissue_count

    def get_sample_date(self):
        date_no_z = self.sample_date_utc.rstrip('Z')
        sample_date = datetime.datetime.strptime(date_no_z, '%Y-%m-%dT%H:%M:%S')
        return sample_date

    def get_discrimination_factor(self,predator_delta13c):
        average_delta13c_sample2 = self.average_delta13c()
        return predator_delta13c - average_delta13c_sample2


sample1 = PreySample(
    full_species_name = 'Harbor Seal (Phoca vitulina)',
    delta13c_list = [-12.4, -11.3, -10.6, -13.5, -15.8],
    tissue_description = 'Bone collagen, Bone collagen, Muscle, Skin',
    sample_date_utc= '2020-11-16T04:25:03Z'
)


print(sample1.get_common_name())
print(sample1.get_scientific_name())
print(sample1.average_delta13c())
print(sample1.get_tissue_count())
print(sample1.get_sample_date())


sample2 = PreySample(
    full_species_name= 'Pacific pomfret (Brama japonica)',
    delta13c_list = [-16.1, -17.8, -19.6, -19.1, -18.0],
    tissue_description = 'whole animal',
    sample_date_utc= '2020-11-17T05:00:02Z'
)

print(sample2.get_discrimination_factor(predator_delta13c = -15.5))


# Finished
