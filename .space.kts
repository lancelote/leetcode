job("Warmup data for Fleet") {
    startOn {
        gitPush {
            branchFilter {
                +"refs/heads/main"
            }
        }
    }
    warmup(ide = Ide.Fleet) {
        scriptLocation = "./dev-env-warmup.sh"
        ideVersion = IdeVersion.LatestOfQuality("Stable")
    }
}
