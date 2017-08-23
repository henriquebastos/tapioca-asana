# coding: utf-8

RESOURCE_MAPPING = {
    'attachment': {
        'resource': 'attachments/{id}',
        'docs': 'https://asana.com/developers/api-reference/attachments#get-single',
        'methods': ['GET']
    },
    'task_attachments': {
        'resource': 'tasks/{id}/attachments',
        'docs': 'https://asana.com/developers/api-reference/attachments#get-all-task',
        'methods': ['GET', 'POST']
    },
    'project_custom_field_settings': {
        'resource': 'projects/{id}/custom_field_settings',
        'docs': 'https://asana.com/developers/api-reference/attachments#get-single',
        'methods': ['GET']
    },
    'custom_field': {
        'resource': 'custom_fields/custom-field-id',
        'docs': 'https://asana.com/developers/api-reference/custom_fields#get-single',
        'methods': ['GET']
    },
    'custom_field': {
        'resource': 'workspaces/{id}/custom_fields',
        'docs': 'https://asana.com/developers/api-reference/custom_fields#query-metadata',
        'methods': ['GET']
    },
    'project_create': {
        'resource': 'projects',
        'docs': 'https://asana.com/developers/api-reference/projects#create',
        'methods': ['POST']
    },
    'workspace_create_project': {
        'resource': 'workspaces/{id}/projects',
        'docs': 'https://asana.com/developers/api-reference/projects#create',
        'methods': ['POST']
    },
    'team_create_project': {
        'resource': 'teams/{id}/projects',
        'docs': 'https://asana.com/developers/api-reference/projects#create',
        'methods': ['POST']
    },
    'project': {
        'resource': 'projects/{id}',
        'docs': 'https://asana.com/developers/api-reference/projects#get-single',
        'methods': ['GET', 'PUT', 'DELETE']
    },
    'project_tasks': {
        'resource': 'projects/{id}/tasks',
        'docs': 'https://asana.com/developers/api-reference/projects#get-tasks',
        'methods': ['GET']
    },
    'projects': {
        'resource': 'projects',
        'docs': 'https://asana.com/developers/api-reference/projects#query',
        'methods': ['GET']
    },
    'workspace_projects': {
        'resource': 'workspaces/{id}/projects',
        'docs': 'https://asana.com/developers/api-reference/projects',
        'methods': ['GET']
    },
    'team_projects': {
        'resource': 'teams/{id}/projects',
        'docs': 'https://asana.com/developers/api-reference/projects',
        'methods': ['GET']
    },
    'project_add_custom_field_setting': {
        'resource': 'projects/{id}/addCustomFieldSetting',
        'docs': 'https://asana.com/developers/api-reference/projects#custom-field-settings',
        'methods': ['POST']
    },
    'project_remove_custom_field_setting': {
        'resource': 'projects/{id}/removeCustomFieldSetting',
        'docs': 'https://asana.com/developers/api-reference/projects#custom-field-settings',
        'methods': ['POST']
    },
    'project_create_section': {
        'resource': 'projects/{id}/sections',
        'docs': 'https://asana.com/developers/api-reference/sections',
        'methods': ['POST']
    },
    'project_sections': {
        'resource': 'projects/{id}/sections',
        'docs': 'https://asana.com/developers/api-reference/sections',
        'methods': ['GET']
    },
    'section': {
        'resource': 'sections/{id}',
        'docs': 'https://asana.com/developers/api-reference/sections#get-single',
        'methods': ['GET', 'PUT', 'DELETE']
    },
    'project_insert_section': {
        'resource': 'projects/{id}/sections/insert',
        'docs': 'https://asana.com/developers/api-reference/sections#reorder',
        'methods': ['POST']
    },

    # Tasks
    'task_create': {
        'resource': 'tasks',
        'docs': 'https://asana.com/developers/api-reference/tasks#create',
        'methods': ['POST']
    },
    'workspace_create_task': {
        'resource': 'workspaces/{id}/tasks',
        'docs': 'https://asana.com/developers/api-reference/tasks#create',
        'methods': ['POST']
    },
    'task': {
        'resource': 'tasks/{id}',
        'docs': 'https://asana.com/developers/api-reference/tasks#get',
        'methods': ['GET', 'PUT', 'DELETE']
    },
    'project_tasks': {
        'resource': 'projects/{id}/tasks',
        'docs': 'https://asana.com/developers/api-reference/tasks#query',
        'methods': ['GET']
    },
    'tag_tasks': {
        'resource': 'tags/{id}/tasks',
        'docs': 'https://asana.com/developers/api-reference/tasks#query',
        'methods': ['GET']
    },
    'section_tasks': {
        'resource': 'sections/{id}/tasks',
        'docs': 'https://asana.com/developers/api-reference/tasks#query',
        'methods': ['GET']
    },
    'tasks': {
        'resource': 'tasks',
        'docs': 'https://asana.com/developers/api-reference/tasks#query',
        'methods': ['GET']
    },
    'task_subtasks': {
        'resource': 'tasks/{id}/subtasks',
        'docs': 'https://asana.com/developers/api-reference/tasks#subtasks',
        'methods': ['GET', 'POST']
    },
    'task_setparent': {
        'resource': 'tasks/{id}/setParent',
        'docs': 'https://asana.com/developers/api-reference/tasks#subtasks',
        'methods': ['POST']
    },
    'task_stories': {
        'resource': 'tasks/{id}/stories',
        'docs': 'https://asana.com/developers/api-reference/tasks#stories',
        'methods': ['GET', 'POST']
    },
    'task_projects': {
        'resource': 'tasks/{id}/projects',
        'docs': 'https://asana.com/developers/api-reference/tasks#projects',
        'methods': ['GET']
    },
    'task_add_project': {
        'resource': 'tasks/{id}/addProject',
        'docs': 'https://asana.com/developers/api-reference/tasks#projects',
        'methods': ['POST']
    },
    'task_remove_project': {
        'resource': 'tasks/{id}/addProject',
        'docs': 'https://asana.com/developers/api-reference/tasks#projects',
        'methods': ['POST']
    },
    'task_tags': {
        'resource': 'tasks/{id}/tags',
        'docs': 'https://asana.com/developers/api-reference/tasks#tags',
        'methods': ['GET']
    },
    'task_add_tag': {
        'resource': 'tasks/{id}/addTag',
        'docs': 'https://asana.com/developers/api-reference/tasks#tags',
        'methods': ['POST']
    },
    'task_remove_tag': {
        'resource': 'tasks/{id}/addTag',
        'docs': 'https://asana.com/developers/api-reference/tasks#tags',
        'methods': ['POST']
    },
    'task_add_followers': {
        'resource': 'tasks/{id}/addFollowers',
        'docs': 'https://asana.com/developers/api-reference/tasks#followers',
        'methods': ['POST']
    },
    'task_remove_tag': {
        'resource': 'tasks/{id}/removeFollowers',
        'docs': 'https://asana.com/developers/api-reference/tasks#followers',
        'methods': ['POST']
    },
    'me': {
        'resource': 'users/me',
        'docs': 'https://asana.com/developers/api-reference/users#get-single',
        'methods': ['GET']
    },
    'user': {
        'resource': 'users/{id}',
        'docs': 'https://asana.com/developers/api-reference/users#get-single',
        'methods': ['GET']
    },
    'users': {
        'resource': 'users',
        'docs': 'https://asana.com/developers/api-reference/users#get-all',
        'methods': ['GET']
    },
    'workspace_users': {
        'resource': 'workspaces/{id}/users',
        'docs': 'https://asana.com/developers/api-reference/users#get-all',
        'methods': ['GET']
    },
    'workspace': {
        'resource': 'workspaces/{id}',
        'docs': 'https://asana.com/developers/api-reference/workspaces#get',
        'methods': ['GET', 'PUT']
    },
    'workspaces': {
        'resource': 'workspaces',
        'docs': 'https://asana.com/developers/api-reference/workspaces#get',
        'methods': ['GET']
    },
    'workspace_add_users': {
        'resource': 'workspaces/{id}/addUsers',
        'docs': 'https://asana.com/developers/api-reference/workspaces#user-mgmt',
        'methods': ['POST']
    },
    'workspace_remove_users': {
        'resource': 'workspaces/{id}/addUsers',
        'docs': 'https://asana.com/developers/api-reference/workspaces#user-mgmt',
        'methods': ['POST']
    },
}

