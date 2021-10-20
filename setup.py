from setuptools import setup


setup(
    name='cldfbench_chacon_and_list2015',
    py_modules=['cldfbench_chacon_and_list2015'],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'cldfbench.dataset': [
            'chacon_and_list2015=cldfbench_chacon_and_list2015:Dataset',
        ]
    },
    install_requires=[
        'cldfbench',
    ],
    extras_require={
        'test': [
            'pytest-cldf',
        ],
    },
)
