# Grepper Python Client
The Grepper Python library provides convenient access to the Grepper API from applications written in the Python language.

## Requirements
Python 3.7 and later.

## PIP
```
pip install grepper-python
```

## Manual Installation
```bash
git clone https://github.com/CantCode023/grepper-python
cd grepper-python
python setup.py install
```


# Usage

## Initialising a new Grepper Class
The following code initialises a new `Grepper` Class.

```py
from grepper_python import Grepper

grepper = Grepper("Your grepper API Key")
```
> Visit [Grepper Account Settings](https://www.grepper.com/app/settings-account.php) to get your API key.


## GrepperAnswer Type Class Reference 
```py
class GrepperAnswer:
    id: int
    content: str
    author_name: str
    author_profile_url: str
    title: str
    upvotes: int
    downvotes: int
```
Refer the above type class whenever you see `GrepperAnswer`

---
## 1. Search function

This function searches all answers based on a query.

### Required parameters

1. ``query (str, optional)``: Query to search through answer titles.
2. ``similarity (Optional[int], optional)``: How similar the query has to be to the answer title. 1-100 where 1 is really loose matching and 100 is really strict/tight match. Defaults to 60.

### Returned value

GrepperAnswer

### Example:

```py
from grepper_python import Grepper

grepper = Grepper("YOUR_API_KEY")
data = grepper.search("git abort command")

# Returns list of GrepperAnswer objects
for answer in data:
		print(answer.id)
		print(answer.content)
		print(answer.author_name)
		print(answer.author_profile_url)
		print(answer.title)
		print(answer.upvotes)
		print(answer.downvotes)
```

### Output

```
674394
git merge --abort
git rebase --abort 
# if you are still into some command on git and got back # 
Magnificent Moose
https://www.grepper.com/profile/mou-biswas
abort a git command
0
0
```
---

## 2. fetch_answer
This function returns an answer specified by the id.

### Required parameters
 - `id (int, required)`: The id for the specified answer. ex: 504956.
### Result 
fetch_answer returns `GrepperAnswer` type class on successful search.

### Examples
```py
grepper = Grepper("YOUR_API_KEY")
answer = grepper.fetch_answer(504956)
print(answer)
```
### Output
```py
{
		"id": 504956,
		"content": "var arr=[1,2,3];\narr.reverse().forEach(x=> console.log(x))",
		"author_name": "Yanislav Ivanov",
		"author_profile_url": "https://www.grepper.com/profile/yanislav-ivanov-r2lfrl14s6xy",
		"title": "js loop array back",
		"upvotes": 2,
		"object": "answer",
		"downvotes": 2
}
```
---

## 3. update_answer
This function updates/edits the answer of specified id.
- `NOTE:` This endpoint is in progress and not yet available according to grepper API docs.

### Required parameters
 - `id (int, required)`: The id for the specified answer. ex: "504956 ".
 - `answer (str, required)`: The answer you want it to update to. ex "new answer content here".

### Result
returns a `Dict`

### Example
```py
grepper = Grepper("YOUR_API_KEY")
result = grepper.update_answer(id="504956",answer="The new edited answer")
print(result)
```

### Output
```py
{
		id: 2,
		success: "true"
}
```
---
