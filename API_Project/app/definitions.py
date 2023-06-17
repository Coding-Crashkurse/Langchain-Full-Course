function_definitions = [
    {
        "name": "get_todos",
        "description": "Get a list of todos, optionally filtered by their completion status",
        "parameters": {
            "type": "object",
            "properties": {
                "completed": {
                    "type": "boolean",
                    "description": "Whether to only return completed todos",
                },
            },
            "required": [],
        },
    },
    {
        "name": "create_todo",
        "description": "Create a new todo",
        "parameters": {
            "type": "object",
            "properties": {
                "todo": {
                    "type": "object",
                    "description": "The new todo to be created",
                    "properties": {
                        "id": {
                            "type": "integer",
                            "description": "The id of the todo",
                        },
                        "task": {
                            "type": "string",
                            "description": "The task of the todo",
                        },
                        "is_completed": {
                            "type": "boolean",
                            "description": "Whether the task is completed",
                            "default": False,
                        },
                    },
                    "required": ["task"],
                },
            },
            "required": ["todo"],
        },
    },
    {
        "name": "update_todo",
        "description": "Update an existing todo",
        "parameters": {
            "type": "object",
            "properties": {
                "id": {
                    "type": "integer",
                    "description": "The id of the todo to update",
                },
                "todo": {
                    "type": "object",
                    "description": "The updated todo",
                    "properties": {
                        "task": {
                            "type": "string",
                            "description": "The updated task of the todo",
                        },
                        "is_completed": {
                            "type": "boolean",
                            "description": "The updated completion status of the task",
                        },
                    },
                    "required": ["task"],
                },
            },
            "required": ["id", "todo"],
        },
    },
    {
        "name": "delete_todo",
        "description": "Delete an existing todo",
        "parameters": {
            "type": "object",
            "properties": {
                "id": {
                    "type": "integer",
                    "description": "The id of the todo to delete",
                },
            },
            "required": ["id"],
        },
    },
    {
        "name": "delete_all_todos",
        "description": "Delete all existing todos",
        "parameters": {"type": "object", "properties": {}, "required": []},
    },
]
