job("My project warmup data") {
    startOn {
        gitPush {
            branchFilter {
                +"refs/heads/main"
            }
        }
    }
    warmup(ide = Ide.Fleet, profileId = "fleet") {
        scriptLocation = "./dev-env-warmup.sh"
    }
}