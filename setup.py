import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()
    
REPO_NAME = "finwhizplus"
AUTHOR_USER_NAME = "supratimdc123"
SRC_REPO = "finwhizplus"
AUTHOR_EMAIL = "supratimdc123@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version='0.1',
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A Python library for financial data analysis and visualization.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)