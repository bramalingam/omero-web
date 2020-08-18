#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2016 University of Dundee & Open Microscopy Environment.
# All rights reserved.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""Handles all 'api' urls."""

from django.urls import path
from omeroweb.api import views
from omeroweb.webgateway.views import LoginView
from . import api_settings
import re

versions = '|'.join([re.escape(v)
                    for v in api_settings.API_VERSIONS])

api_versions = path('', views.api_versions, name='api_versions')

api_base = path('v%s/' % versions,
               views.api_base,
               name='api_base')
"""
GET various urls listed below
"""

api_token = path('v%s/token/' % versions,
                views.api_token,
                name='api_token')
"""
GET the CSRF token for this session. Needs to be included
in header with all POST, PUT & DELETE requests
"""

api_servers = path('v%s/servers/' % versions,
                  views.api_servers,
                  name='api_servers')
"""
GET list of available OMERO servers to login to.
"""

api_login = path('v%s/login/' % versions,
                LoginView.as_view(),
                name='api_login')
"""
Login to OMERO. POST with 'username', 'password' and 'server' index
"""

api_save = path('v%s/m/save/' % versions,
               views.SaveView.as_view(),
               name='api_save')
"""
POST to create a new object or PUT to update existing object.
In both cases content body encodes json data.
"""

api_projects = path('v%s/m/projects/' % versions,
                   views.ProjectsView.as_view(),
                   name='api_projects')
"""
GET all projects, using omero-marshal to generate json
"""

api_project = path(
    'v%s/m/projects/(<int:object_id>)/' % versions,
    views.ProjectView.as_view(),
    name='api_project')
"""
Project url to GET or DELETE a single Project
"""

api_datasets = path('v%s/m/datasets/' % versions,
                   views.DatasetsView.as_view(),
                   name='api_datasets')
"""
GET all datasets, using omero-marshal to generate json
"""

api_project_datasets = path(
    'v%s/m/projects/'
    '<int:project_id>/datasets/' % versions,
    views.DatasetsView.as_view(),
    name='api_project_datasets')
"""
GET Datasets in Project, using omero-marshal to generate json
"""

api_dataset = path(
    'v%s/m/datasets/<int:object_id>)/' % versions,
    views.DatasetView.as_view(),
    name='api_dataset')
"""
Dataset url to GET or DELETE a single Dataset
"""

api_images = path('v%s/m/images/' % versions,
                 views.ImagesView.as_view(),
                 name='api_images')
"""
GET all images, using omero-marshal to generate json
"""

api_dataset_images = path(
    'v%s/m/datasets/'
    '<int:dataset_id>/images/' % versions,
    views.ImagesView.as_view(),
    name='api_dataset_images')
"""
GET Images in Dataset, using omero-marshal to generate json
"""

api_dataset_projects = path(
    'v%s/m/datasets/'
    '<int:dataset_id>/projects/' % versions,
    views.ProjectsView.as_view(),
    name='api_dataset_projects')
"""
GET Projects that contain a Dataset, using omero-marshal to generate json
"""

api_image = path(
    'v%s/m/images/<int:object_id>/' % versions,
    views.ImageView.as_view(),
    name='api_image')
"""
Image url to GET or DELETE a single Image
"""

api_image_datasets = path(
    'v%s/m/images/'
    '<int:image_id>/datasets/' % versions,
    views.DatasetsView.as_view(),
    name='api_image_datasets')
"""
GET Datasets that contain an Image, using omero-marshal to generate json
"""

api_screen = path(
    'v%s/m/screens/<int:object_id>/' % versions,
    views.ScreenView.as_view(),
    name='api_screen')
"""
Screen url to GET or DELETE a single Screen
"""

api_screens = path('v%s/m/screens/' % versions,
                  views.ScreensView.as_view(),
                  name='api_screens')
"""
GET all screens, using omero-marshal to generate json
"""

api_plates = path('v%s/m/plates/' % versions,
                 views.PlatesView.as_view(),
                 name='api_plates')
"""
GET all plates, using omero-marshal to generate json
"""

api_screen_plates = path(
    'v%s/m/screens/'
    '<int:screen_id>/plates/' % versions,
    views.PlatesView.as_view(),
    name='api_screen_plates')
"""
GET Plates in Screen, using omero-marshal to generate json
"""

api_well_plates = path(
    'v%s/m/wells/'
    '<int:well_id>/plates/' % versions,
    views.PlatesView.as_view(),
    name='api_well_plates')
"""
GET Plates that contain a Well, using omero-marshal to generate json
"""

api_plate = path(
    'v%s/m/plates/<int:object_id>/' % versions,
    views.PlateView.as_view(),
    name='api_plate')
"""
Plate url to GET or DELETE a single Plate
"""

api_wells = path('v%s/m/wells/' % versions,
                views.WellsView.as_view(),
                name='api_wells')
"""
GET all wells, using omero-marshal to generate json
"""

api_plate_plateacquisitions = path(
    'v%s/m/plates/'
    '<int:plate_id>/plateacquisitions/' % versions,
    views.PlateAcquisitionsView.as_view(),
    name='api_plate_plateacquisitions')
"""
GET PlateAcquisitions in Plate, using omero-marshal to generate json
"""

api_plateacquisition = path(
    'v%s/m/plateacquisitions/'
    '<int:object_id>/' % versions,
    views.PlateAcquisitionView.as_view(),
    name='api_plateacquisition')
"""
Well url to GET or DELETE a single Well
"""

api_plateacquisition_wellsampleindex_wells = path(
    'v%s/m/plateacquisitions/'
    '<int:plateacquisition_id>/wellsampleindex/'
    '<int:index>/wells/' % versions,
    views.WellsView.as_view(),
    name='api_plateacquisition_wellsampleindex_wells')
"""
GET Wells from a single Index in PlateAcquisition
"""

api_plate_wellsampleindex_wells = path(
    'v%s/m/plates/'
    '<int:plate_id>/wellsampleindex/'
    '<int:index>/wells/' % versions,
    views.WellsView.as_view(),
    name='api_plate_wellsampleindex_wells')
"""
GET Wells from a single Index in Plate
"""

api_plate_wells = path(
    'v%s/m/plates/'
    '<int:plate_id>/wells/' % versions,
    views.WellsView.as_view(),
    name='api_plate_wells')
"""
GET Wells in Plate, using omero-marshal to generate json
"""

api_plateacquisition_wells = path(
    r'v%s/m/plateacquisitions/'
    '<int:plateacquisition_id>/wells/' % versions,
    views.WellsView.as_view(),
    name='api_plateacquisition_wells')
"""
GET Wells in Plate, using omero-marshal to generate json
"""

api_well = path(
    'v%s/m/wells/<int:object_id>/' % versions,
    views.WellView.as_view(),
    name='api_well')
"""
Well url to GET or DELETE a single Well
"""

api_plate_screens = path(
    'v%s/m/plates/'
    '<int:plate_id>/screens/' % versions,
    views.ScreensView.as_view(),
    name='api_plate_screens')
"""
GET Screens that contain a Plate, using omero-marshal to generate json
"""

api_rois = path('v%s/m/rois/' % versions,
               views.RoisView.as_view(),
               name='api_rois')
"""
GET all rois, using omero-marshal to generate json
"""

api_roi = path(
    'v%s/m/rois/<int:object_id>/' % versions,
    views.RoiView.as_view(),
    name='api_roi')
"""
ROI url to GET or DELETE a single ROI
"""

api_image_rois = path(
    'v%s/m/images/'
    '<int:image_id>/rois/' % versions,
    views.RoisView.as_view(),
    name='api_image_rois')
"""
GET ROIs that belong to an Image, using omero-marshal to generate json
"""

api_experimenters = path('v%s/m/experimenters/' % versions,
                        views.ExperimentersView.as_view(),
                        name='api_experimenters')
"""
GET Experimenters, using omero-marshal to generate json
"""

api_experimenter = path('v%s/m/experimenters/'
                       '<int:object_id>/' % versions,
                       views.ExperimenterView.as_view(),
                       name='api_experimenter')
"""
GET Experimenter, using omero-marshal to generate json
"""

api_group_experimenters = path(
    'v%s/m/experimentergroups/<int:group_id>'
    '/experimenters/' % versions,
    views.ExperimentersView.as_view(),
    name='api_experimentergroup_experimenters')
"""
GET Experimenters in a Group, using omero-marshal to generate json
"""

api_groups = path('v%s/m/experimentergroups/' % versions,
                 views.ExperimenterGroupsView.as_view(),
                 name='api_experimentergroups')
"""
GET ExperimenterGroups, using omero-marshal to generate json
"""

api_group = path('v%s/m/experimentergroups/'
                '<int:object_id>/' % versions,
                views.ExperimenterGroupView.as_view(),
                name='api_experimentergroup')
"""
GET ExperimenterGroup, using omero-marshal to generate json
"""

api_experimenter_groups = path(
    'v%s/m/experimenters/<int:experimenter_id>'
    '/experimentergroups/' % versions,
    views.ExperimenterGroupsView.as_view(),
    name='api_experimenter_experimentergroups')
"""
GET Groups that an Experimenter is in, using omero-marshal to generate json
"""

urlpatterns = [
    api_versions,
    api_base,
    api_token,
    api_servers,
    api_login,
    api_save,
    api_projects,
    api_project,
    api_datasets,
    api_project_datasets,
    api_dataset,
    api_images,
    api_dataset_images,
    api_dataset_projects,
    api_image,
    api_image_datasets,
    api_screen,
    api_screens,
    api_plates,
    api_screen_plates,
    api_well_plates,
    api_plate,
    api_wells,
    api_plate_plateacquisitions,
    api_plateacquisition,
    api_plateacquisition_wellsampleindex_wells,
    api_plate_wellsampleindex_wells,
    api_plate_wells,
    api_plateacquisition_wells,
    api_well,
    api_plate_screens,
    api_rois,
    api_roi,
    api_image_rois,
    api_experimenters,
    api_experimenter,
    api_group_experimenters,
    api_groups,
    api_group,
    api_experimenter_groups,
]
