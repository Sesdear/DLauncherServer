# Manifests blanks

## /api/indexes
#### Indexes manifest

``` Json
{
    "servers": [
        "ExampleServer1",
        "ExampleServer2",
        "ExampleServer3",
        "ExampleServer4",
    ]
}
```
`AvalibleServers` contains pathes to data files for servers
Example path: `AvalibleServers[1]` -> `/api/servers/{AvalibleServers[1]}/data`

## /api/ExampleServer/
#### `/api/servers/ExampleServer/data` Data inforamtion manifest

``` Json
{
    "ServerName":"Server name 1", 
    "Description":"Very intresting description",
    "ImagePath":"/files/ExampleServer/icon.png",
    "MinecraftVersion":"1.20.1",
    "MinecraftModLoader":"forge",
    "MinecraftModLoaderVersion":"4.19.1",
    "FilesRepoURL":"https://example-git.com/repo.git"
}

```
Server data manifest contains:
- `ServerName: string`
- `Description: string`
- `ImagePath: string` (if exist)
- `MinecraftVersion: string`
- `MinecraftModLoader: string`
- `MinecraftModLoaderVersion: string`
- `FilesRepoURL: string`



## `/api/minecraft_repos` 
#### Mineraft repos information manifest

``` Json
{
    "1.7.10": "https://git-repo-to-1710-minecraft-repo/1710.git",
    "1.12.2": "https://git-repo-to-1122-minecraft-repo/1122.git",
    "1.16.5": "https://git-repo-to-1165-minecraft-repo/1165.git",
    "1.18.2": "https://git-repo-to-1182-minecraft-repo/1182.git",
    "1.20.1": "https://git-repo-to-1201-minecraft-repo/1201.git",
}
```
This manifest contains self hosted minecraft repositories, if you need to change default minecraft repositories use this (always need for DLauncher4 1.5.0.0 or above)


