# Etrian Odyssey Archipelago (AP)

The setup guide is coming soon.

Please open any issues related to the randomizer in this repository and not one of the related ones.

## Running from Source

First, become familiar with [running archipelago from source documentation](https://github.com/ArchipelagoMW/Archipelago/blob/main/docs/running%20from%20source.md).

Once that is done, do not clone this repository, instead do a clone of [this repository](https://github.com/TheMasterZelda/Archipelago), using the command `git clone --recurse-submodules https://github.com/TheMasterZelda/Archipelago`.

Once done, you can now contribute or run this apworld from `.\worlds\etrian_odyssey\`.

Everything else is standard running archipelago from source, except for the use of submodule.

If the submodule reference get desynced, please notify me via Discord so it can get fixed as fast as possible.

## Contributing

If you want to contribute, you are more than welcome to. Join the Archipelago discord and look for the Etrian Odyssey channel, where I will direct however wants to help towards everything that currently need attention.

Help is welcome not only from a developper perspective but also for logic balancing and testing.

## APWorld Project Structure

The project is structured in a very simple way:

- Code specific to Archipelago objects are in the root directory.
- Game Data and basic data parsing functions go in the `\data` directory.
- The more complex logic processing code goes in the `\logic` directory. Rules cannot be here, but can refer to here.

## Related Projects

- [Patcher](https://github.com/TheMasterZelda/etrian-odyssey-1-archipelago-patcher)
- [Binary Patch](https://github.com/TheMasterZelda/etrian-odyssey-1-archipelago-patch)
- [Parent Repository](https://github.com/TheMasterZelda/Archipelago)
- [Archipelago Core](https://github.com/ArchipelagoMW/Archipelago)

## Credits

- Thanks to Slimey for the early help in figuring out DS Modding.
- Thanks to the Archipelago dev community for being welcoming and helping.
- Thanks to the Etrian Odyssey community for helping with reverse engineering.
- Thanks to anyone else I forgot to mention for helping.