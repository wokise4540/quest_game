from django.shortcuts import render

from quest_game.models import Story


def home(request):
    stories = Story.objects.filter()
    return render(request, 'home.html', {"story_list": stories})


def story_homepage(request, story_id):
    story = Story.objects.get(id=story_id)
    return render(request, 'story_homepage.html', {"story": story})


def story_progress(request, story_id, story_step):
    story = Story.objects.get(id=story_id)
    que = story.data[str(story_step)]["que"]
    answ = story.data[str(story_step)]["ans"]
    return render(request, 'story_progress.html', {"story": story, "question": que, "answers": answ})