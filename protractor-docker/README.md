# Example of how to use Protractor and Docker together

### How to use

```sh
docker-compose run --rm protractor
```

### Files and folders
```
.
├── docker-compose.yml     # The main "docker-compose" file
├── Dockerfile             # Dockerfile with protractor installed
└── example                # Example folder
    ├── protractor.conf.js # Protractor configuration file
    └── todo-spec.js       # Example of test
```
