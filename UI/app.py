from h2o_wave import Q, main, app, ui
import requests

base_url = "http://api:8000/"

def make_request(sentence: str):
    data = {"sentence": sentence}
    y = requests.post(base_url, json=data)
    return y.json()

@app('/')
async def user_text(q: Q):
    if q.args.NERd:
        result = make_request(sentence = q.args.text)
        q.page['form'] = ui.form_card(box='1 1 3 10', items=[
        ui.text_l('spaCy, FastAPI, Docker, and h2o wave NER'),
        ui.text(str(result)),
        ui.button(name='goback', label='go back', primary=True),
    ])
        await q.page.save()
    elif q.args.goback:
        q.page['form'] = ui.form_card(box='1 1 3 10', items=[
        ui.text_l('spaCy, FastAPI, Docker, and h2o wave NER'),
        ui.textbox(name='text', label='Insert Text to be NERded', multiline=True),
        ui.button(name='NERd', label='NERd', primary=True),
    ])
        await q.page.save()
    else:
        q.page['form'] = ui.form_card(box='1 1 3 10', items=[
        ui.text_l('spaCy, FastAPI, Docker, and h2o wave NER'),
        ui.textbox(name='text', label='Insert Text to be NERded', multiline=True),
        ui.button(name='NERd', label='NERd', primary=True),
    ])
        await q.page.save()
