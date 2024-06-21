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

## Getting Grepper API key
Visit [Grepper Account Settings](https://www.grepper.com/app/settings-account.php) to get your API key.

## Initialising a new Grepper Class
```py
grepper = Grepper("Your grepper API Key")
```
The following code initialises a new `Grepper` Class.

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
## Search function

This function searches all answers based on a query.

## Arguements required

1. ``query (str, optional)``: Query to search through answer titles.
2. ``similarity (Optional[int], optional)``: How similar the query has to be to the answer title. 1-100 where 1 is really loose matching and 100 is really strict/tight match. Defaults to 60.

## Returned value

GrepperAnswer

## Example of the function by using in a code:

```py
import grepper_python

grepper = grepper_python.Grepper("YOUR API")

data = grepper.search("cat videos")
for i in data:
    print(i)
```

## Output

```py

GrepperAnswer(id=667265, content='{"tags":[{"tag":"p","content":"Get back to work"}]}', 

author_name='Smyth Family', 

author_profile_url='https://www.grepper.com/profile/smyth-family',

 title='cat videos', 

 upvotes=4, 

 downvotes=0)

```
---
# fetch_answer
This function returns an answer specified by the id.
### Arguments
 - `id (int, required)`: The id for the specified answer. ex: "504956 ".
### Result 
fetch_answer returns `GrepperAnswer` type class on successful search.

### Examples
#### Example fetch_answer
```py
grepper = Grepper("your-grepper-api-key")
answer = grepper.fetch_answer("504956")
print(answer)
```
### Example Output
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

# update_answer
This function updates/edits the answer of specified id.
- `NOTE:` This endpoint is in progress and not yet available according to grepper API docs.
### Arguments
 - `id (int, required)`: The id for the specified answer. ex: "504956 ".
 - `answer (str, required)`: The answer you want it to update to. ex "new answer content here".
### Result
returns a `Dict`

### Examples
#### Example update_answer
```py
grepper = Grepper("your-grepper-api-key")
result = grepper.update_answer(id="504956",answer="The new edited answer")
print(result)
```
#### Example Result
```py
{
 id: 2,
 success: "true"
}
```
---
