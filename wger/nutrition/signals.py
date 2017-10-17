# -*- coding: utf-8 -*-

# This file is part of wger Workout Manager.
#
# wger Workout Manager is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# wger Workout Manager is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License

from django.db.models.signals import post_save
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.core.cache import cache

from wger.nutrition.models import NutritionPlan, Meal, MealItem

@receiver(post_delete, sender=NutritionPlan)
@receiver(post_delete, sender=Meal)
@receiver(post_delete, sender=MealItem)
def post_delete_activity(sender, instance, **kwargs):
    '''
      Signal: post_delete
      Sender: NutritionPlan, Meal, MealItem
    '''
    plan = instance.get_owner_object()
    cache.delete('nutrition_plans-{0}'.format(plan.id))

@receiver(post_save, sender=NutritionPlan)
@receiver(post_save, sender=Meal)
@receiver(post_save, sender=MealItem)
def post_save_activity(sender, instance, **kwargs):
    '''
      Signal: post_save
      Sender: NutritionPlan, Meal, MealItem
    '''
    plan = instance.get_owner_object()
    cache.delete('nutrition_values-{0}'.format(plan.id))
