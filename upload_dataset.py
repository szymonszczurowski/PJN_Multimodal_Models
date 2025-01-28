import datasets


ds = datasets.load_dataset("HuggingFaceM4/ChartQA")

ds_train = ds['train'].filter(lambda x: x["human_or_machine"] == 0)
ds_test = ds['test'].filter(lambda x: x["human_or_machine"] == 0)
ds_val = ds['val'].filter(lambda x: x["human_or_machine"] == 0)

sampled_train = ds_train.shuffle(seed=42).select(range(1200))
sampled_test = ds_test.shuffle(seed=42).select(range(500))
sampled_val = ds_val.shuffle(seed=42).select(range(500))

sampled_ds = datasets.DatasetDict({
    'train': sampled_train,
    'val': sampled_val,
    'test': sampled_test
})

final_ds = sampled_ds.remove_columns("human_or_machine")

final_ds.push_to_hub("krowiemlekommm/PJN_CHARTS")